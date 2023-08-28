from scrapper.spiders.adapters.base import BaseAdapter


class HimalayasAdapter(BaseAdapter):
    selectors = {
        "link": "//ul[@id='card-group']/li[@data-action='click->card#goToPage']/@data-path",
        "next_page": "//a[@data-action='click->instantsearch#changePage'][contains(@class, 'btn')][@rel='next']/@href",
        "jobpost": {
            "title": "//h1/text()",
            "description": "//div[@class='trix-content']",
            "origin_url": "//meta[@property='og:url']/@content",
            "company_link": "//span/a[contains(@href, 'companies')]/@href",
            "categories": "//label[contains(text(), 'Job categories')]/..//span/text()"
        },
        "company": {
            "name": "//h1//span/text()",
            "website": "//span[contains(text(), 'Visit')]/../@href",
            "logo_url": "//section//div[contains(@class, 'avatar-logo')]/img[contains(@title, 'logo')]/@src",
            "origin_url": "//meta[@property='og:url']/@content",
            "description": "//div[@class='trix-content']",
        },
    }
