from scrapper.spiders.adapters.base import BaseAdapter


class HimalayasAdapter(BaseAdapter):
    selectors = {
        "link": "//article//a[contains(@href,'/jobs/')][contains(@href,'/companies/')]/@href",
        "next_page": "//nav[@aria-label='pagination']//span[contains(text(), 'Next')]/../@href",
        "jobpost": {
            "title": "//h1/text()",
            "description": "//div[@class='border-b border-gray-200 pb-8 md:pb-12']//article",
            "company_link": "//section//a[contains(@href, '/companies/')]/@href",
            "categories": "//h3[contains(text(), 'Skills')]/..//span/text()",
        },
        "company": {
            "name": "//h1/text()",
            "website": "//a[contains(text(), 'Visit')]/@href",
            "logo_url": "//img[@data-nimg='fill']/@src",
            "description": "//div[@class='flex-shrink-0 xl:w-[48rem]']//article//article",
        },
    }
    root_page = "https://himalayas.app/jobs"
    pages = [
        "/jobs/software-engineering",
        "/jobs/software-development",
        "/jobs/software-architecture",
    ]
