import scrapy
from .adapters import ADAPTERS


class RecolectorSpider(scrapy.Spider):
    name = "recolector"
    record = None

    def start_requests(self):
        for adapter in ADAPTERS:
            if not adapter.is_active:
                continue

            yield scrapy.Request(
                adapter.root_page, callback=self.parse, cb_kwargs=dict(adapter=adapter)
            )

    def parse(self, response, adapter):
        for request in adapter.parse(response):
            yield request
