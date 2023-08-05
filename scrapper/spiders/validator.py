import scrapy, json
from pathlib import Path
from urllib.parse import urlparse
from .mixins import ParseMixins
from ..items import WebOriginItem
from .recolector import RecolectorSpider

BASE_DIR = Path(__file__).resolve().parent.parent


class ValidatorSpider(scrapy.Spider, ParseMixins):
    name = "validator"
    jobpost_urls = {}
    recolector = RecolectorSpider

    def start_requests(self):
        with open(BASE_DIR / "websites.json", "r") as jsonfile:
            data = json.loads(jsonfile.read())

            for website in data:
                jobpost_url = self.jobpost_urls.get(urlparse(website['url']).netloc, None)
                
                yield scrapy.Request(
                    website["url"],
                    callback=self.parse,
                    cb_kwargs=dict(
                        website=website,
                        jobpost_url=jobpost_url
                    )
                )

    def parse(self, response, website, jobpost_url):
        weborigin = WebOriginItem(**{
            "name": urlparse(response.url).hostname,
            "website": f"https://{urlparse(response.url).hostname}"
        })

        if jobpost_url:
            yield response.follow(
                jobpost_url,
                callback=self.parse_job,
                cb_kwargs=dict(
                    weborigin=weborigin,
                    website=website
                )
            )

        else:
            yield { "weborigin": weborigin }
