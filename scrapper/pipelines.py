# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from asgiref.sync import sync_to_async
from backend.apps.jobpost.models import JobPost, Company, WebsiteOrigin
from itemadapter import ItemAdapter


class ScrapperPipeline:
    @sync_to_async
    def create_object(self, object, item):
        adapter = ItemAdapter(item)
        return object.objects.get_or_create(**adapter)[0]
    
    async def process_item(self, item, spider):

        weborigin = await self.create_object(WebsiteOrigin, item["weborigin"])
        item["company"]["origin"] = item["jobpost"]["origin"] = weborigin
        item["jobpost"]["company"] = await self.create_object(Company, item["company"])
        await self.create_object(JobPost, item["jobpost"])

        return item
