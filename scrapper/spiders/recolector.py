import scrapy, json
from pathlib import Path
from urllib.parse import urlparse
from .mixins import ParseMixins
from ..items import WebOriginItem

BASE_DIR = Path(__file__).resolve().parent.parent


class RecolectorSpider(scrapy.Spider, ParseMixins):
    name = "recolector"
    inactive_urls = []

    def start_requests(self):
        with open(BASE_DIR / "websites.json", "r") as jsonfile:
            data = json.loads(jsonfile.read())

            for website in data:
                url = f"https://{urlparse(website['url']).hostname}"

                if url in self.inactive_urls:
                    continue

                yield scrapy.Request(
                    website["url"],
                    callback=self.parse,
                    cb_kwargs=dict(website=website)
                )

    def parse(self, response, website):
        jobcards = response.xpath(website["link"]).getall()
        next_page = response.xpath(website["next_page"]).get()
        weborigin = WebOriginItem(**{
            "name": urlparse(response.url).hostname,
            "website":  f"https://{urlparse(response.url).hostname}"
        })
        
        for link in jobcards:
            yield response.follow(
                link,
                callback=self.parse_job,
                cb_kwargs=dict(
                    weborigin=weborigin,
                    website=website
                )
            )

        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse,
                cb_kwargs=dict(website=website)
            )

