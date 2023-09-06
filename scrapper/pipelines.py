# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from urllib.parse import urlparse
from asgiref.sync import sync_to_async
from backend.apps.jobpost.models import JobPost, Company, WebsiteOrigin, Category
from django.core.files import File
from itemadapter import ItemAdapter
from tempfile import NamedTemporaryFile
from .spiders.recolector import RecolectorSpider


class RecolectorPipeline:
    record = None

    @sync_to_async
    def save_image(self, object_field, url):
        if not object_field:
            content = requests.get(url).content

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(content)
            img_temp.flush()

            object_field.save("logo.jpg", File(img_temp), save=True)

    @sync_to_async
    def set_category(self, jobpost, categories):
        jobpost.categories.set(categories)

    @sync_to_async
    def create_object(self, model=None, item=None, count_label=None):
        adapter = ItemAdapter(item)
        item, is_new = model.objects.get_or_create(**adapter)

        if is_new and count_label:
            self.record.add_count(count_label)

        return model.objects.get_or_create(**adapter)[0]

    async def process_item(self, item, spider):
        if not isinstance(spider, RecolectorSpider):
            return item

        if not self.record:
            self.record = spider.record

        weborigin = await self.create_object(WebsiteOrigin, item["weborigin"])
        item["company"]["origin"] = item["jobpost"]["origin"] = weborigin

        item["categories"] = [
            await self.create_object(model=Category, item=category_item)
            for category_item in item["jobpost"].pop("categories")
        ]

        item["jobpost"]["company"] = await self.create_object(
            model=Company, item=item["company"], count_label="companies"
        )

        await self.save_image(item["jobpost"]["company"].logo, item["logo_url"])

        jobpost = await self.create_object(
            model=JobPost, item=item["jobpost"], count_label="jobposts"
        )

        await self.set_category(jobpost, item["categories"])

        return item
