import scrapy, json
from pathlib import Path
from urllib.parse import urlparse
from ..items import JobpostItem, CompanyItem, WebOriginItem

BASE_DIR = Path(__file__).resolve().parent.parent 

class JobpostSpider(scrapy.Spider):
    name = "jobpost"

    def start_requests(self):
        with open(BASE_DIR / "websites.json", "r") as jsonfile:
            data = json.loads(jsonfile.read())

            for website in data:
                yield scrapy.Request(
                    website["url"],
                    callback=self.parse,
                    cb_kwargs=dict(website=website)
                )

    def parse_company(self, response, jobpost, website, weborigin):
        company_config = website["company"]

        company = CompanyItem(**{
            "name": response.xpath(company_config["name"]).get().strip(),
            "website": f"https://{urlparse(response.xpath(company_config['website']).get()).netloc}"
        })
      
        yield {
            "logo_url": response.xpath(company_config['logo_url']).get(),
            "company": company,
            "jobpost": jobpost,
            "weborigin": weborigin
        }

    def parse_job(self, response, website, weborigin):
        jobpost_config = website["jobpost"]
        link = response.xpath(jobpost_config["company_link"]).get()

        jobpost = JobpostItem(**{
            "title": response.xpath(jobpost_config["title"]).get().strip(),
            "description": response.xpath(jobpost_config["description"]).get(),
            "origin_url": response.xpath(jobpost_config["origin_url"]).get()
        })

        yield response.follow(
            link,
            callback=self.parse_company,
            cb_kwargs=dict(
                jobpost=jobpost,
                weborigin=weborigin,
                website=website
            )
        )

    def parse(self, response, website):
        jobcards = response.xpath(website["link"]).getall()
        next_page = response.xpath(website["next_page"]).get()
        weborigin = WebOriginItem(**{
            "name": urlparse(response.url).netloc,
            "website": urlparse(response.url).netloc
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

