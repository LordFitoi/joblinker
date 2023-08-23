import scrapy
from urllib.parse import urlparse
from .adapters import ADAPTERS


class ValidatorSpider(scrapy.Spider):
    name = "validator"
    objects = {}

    def start_requests(self):
        for url, adapter in ADAPTERS.items():
            objects = self.objects.get(urlparse(url).netloc, None)

            if not objects:
                continue

            yield scrapy.Request(
                url,
                callback=self.parse,
                cb_kwargs=dict(adapter=adapter, objects=objects),
            )

    def parse(self, _, adapter, objects):
        for request in adapter.validate(objects):
            yield request
