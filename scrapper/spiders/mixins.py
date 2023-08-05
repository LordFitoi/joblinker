from urllib.parse import urlparse
from ..items import JobpostItem, CompanyItem


class ParseMixins:
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