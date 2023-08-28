import re
from urllib.parse import urlparse
from scrapper.spiders.adapters.base import BaseAdapter


class NoDeskAdapter(BaseAdapter):
    selectors = {
        "link": "//ul[@class='list mv0 pl0']/li//h2/a/@href",
        "next_page": "//a[@data-testid='pagination-page-next']/@href",
        "jobpost": {
            "title": "//h1/text()",
            "description": "//div[@class='grey-800']",
            "company_link": "//h2//a[contains(@href, '/remote-companies/')][@class='link dim grey-700']/@href",
            "origin_url": "//meta[@property='og:url']/@content",
            "categories": "//ul[@class='f9 list mv0 pl0']/li//text()",
        },
        "company": {
            "name": "//h1/text()",
            "website": "//a[@class='dib link dim grey-800 f8 mv0']/@href",
            "logo_url": "//img[@class='bg-white br-100 h9 h10-ns w9 w10-ns mr6-ns shadow-2']/@src",
            "origin_url": "//meta[@property='og:url']/@content",
            "description": "//section[@class='fl grey-800 center-l measure-wide-s measure-wide-l mt8 mt0-ns w-100 w-60-m w-75-l']",
        },
    }

    def get_logo_url(self, response, selector):
        url = super().get_logo_url(response, selector)
        return f"https://{urlparse(response.url).netloc}/{url}"

    def format(self, text):
        text = re.sub('<a.*href="/remote-jobs/"[^>]*>.*</a>', "", text)
        return super().format(text)

    def get_nextpage(self, response):
        return False
