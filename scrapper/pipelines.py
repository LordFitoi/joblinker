# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
from urllib.parse import urlparse
from asgiref.sync import sync_to_async
from backend.apps.jobpost.models import JobPost, Company, WebsiteOrigin
from django.core.files import File
from itemadapter import ItemAdapter
from tempfile import NamedTemporaryFile
from .spiders.recolector import RecolectorSpider


class RecolectorPipeline:
    @sync_to_async
    def save_image(self, object_field, url):
        if not object_field:
            name = f"{urlparse(url).path.split('/')[-1]}.jpg"
            content = requests.get(url).content

            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(content)
            img_temp.flush()

            object_field.save(name, File(img_temp), save=True)

    @sync_to_async
    def get_origin(self, item):
        adapter = ItemAdapter(item)
        return WebsiteOrigin.objects.get(**adapter)

    @sync_to_async
    def create_object(self, object, item):
        adapter = ItemAdapter(item)
        return object.objects.get_or_create(**adapter)[0]
    
    async def process_item(self, item, spider):
        if not isinstance(spider, RecolectorSpider):
            return item

        weborigin = await self.get_origin(item["weborigin"])
        item["company"]["origin"] = item["jobpost"]["origin"] = weborigin
        item["jobpost"]["company"] = await self.create_object(Company, item["company"])

        await self.create_object(JobPost, item["jobpost"])
        await self.save_image(item["jobpost"]["company"].logo, item["logo_url"])

        return item
    
