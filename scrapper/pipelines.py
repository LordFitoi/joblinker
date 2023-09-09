# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from asgiref.sync import sync_to_async
from backend.apps.jobpost.models import JobPost, Company, WebsiteOrigin, Category
from django.core.files import File
from itemadapter import ItemAdapter
from tempfile import NamedTemporaryFile
from .spiders.recolector import RecolectorSpider


class JobpostPipeline:
    record = None

    @sync_to_async
    def get_category(self, item):
        adapter = ItemAdapter(item)

        try:
            return Category.objects.get(name=adapter["name"])
        except Category.DoesNotExist:
            category = Category.objects.create(**adapter)
            self.record.add_count("categories")

            return category

    @sync_to_async
    def get_jobpost(self, item, categories):
        adapter = ItemAdapter(item)

        try:
            return JobPost.objects.get(origin_url=adapter["origin_url"])
        except JobPost.DoesNotExist:
            jobpost = JobPost.objects.create(**adapter)

            self.record.add_count("jobposts")
            jobpost.categories.set(categories)

            return jobpost

    async def __call__(self, item):
        item["categories"] = [
            await self.get_category(category_item)
            for category_item in item["jobpost"].pop("categories")
        ]

        return await self.get_jobpost(item["jobpost"], item["categories"])


class CompanyPipeline:
    record = None

    @sync_to_async
    def save_image(self, company, url):
        if not company.logo:
            content = requests.get(url).content

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(content)
            img_temp.flush()

            company.logo.save("logo.jpg", File(img_temp), save=True)

    @sync_to_async
    def get_object(self, item):
        adapter = ItemAdapter(item)

        try:
            return Company.objects.get(website=adapter["website"])
        except Company.DoesNotExist:
            company = Company.objects.create(**adapter)
            self.record.add_count("companies")

            return company

    async def __call__(self, item):
        company = await self.get_object(item["company"])
        await self.save_image(company, item["logo_url"])

        return company


class RecolectorPipeline:
    record = None
    company_pipeline = CompanyPipeline()
    jobpost_pipeline = JobpostPipeline()

    @sync_to_async
    def get_weborigin(self, item):
        adapter = ItemAdapter(item)

        try:
            return WebsiteOrigin.objects.get(website=adapter["website"])
        except WebsiteOrigin.DoesNotExist:
            return WebsiteOrigin.objects.create(**adapter)

    async def process_item(self, item, spider):
        if not isinstance(spider, RecolectorSpider):
            return item

        if not self.record:
            self.record = spider.record
            self.company_pipeline.record = spider.record
            self.jobpost_pipeline.record = spider.record

        weborigin = await self.get_weborigin(item["weborigin"])
        item["company"]["origin"] = item["jobpost"]["origin"] = weborigin
        item["jobpost"]["company"] = await self.company_pipeline(item)

        return await self.jobpost_pipeline(item)
