
import scrapy
from urllib.parse import urlparse
from scrapper.items import CompanyItem, JobpostItem, WebOriginItem


class BaseAdapter:
    is_active = True
    selectors = {}

    def get_weborigin(self, response):
        return WebOriginItem(**{
            'name': urlparse(response.url).hostname,
            'website':  f'https://{urlparse(response.url).hostname}'
        })
    
    def get_jobpost(self, response):
        selectors = self.selectors['jobpost']

        return JobpostItem(**{
            'title': response.xpath(selectors['title']).get().strip(),
            'description': response.xpath(selectors['description']).get(),
            'origin_url': response.xpath(selectors['origin_url']).get()
        })

    def get_company(self, response):
        selectors = self.selectors['company']
        
        return CompanyItem(**{
            'name': response.xpath(selectors['name']).get().strip(),
            'website': f'https://{urlparse(response.xpath(selectors["website"]).get()).netloc}',
            'description': response.xpath(selectors['description']).get(),
            'origin_url': response.xpath(selectors['origin_url']).get()
        })
    
    def parse_company(self, response, jobpost, weborigin):
        selectors = self.selectors['company']

        yield {
            'logo_url': response.xpath(selectors['logo_url']).get(),
            'company': self.get_company(response),
            'jobpost': jobpost,
            'weborigin': weborigin
        }

    def parse_jobpost(self, response, weborigin):
        yield response.follow(
            response.xpath(self.selectors['jobpost']['company_link']).get(),
            callback=self.parse_company,
            cb_kwargs=dict(
                jobpost=self.get_jobpost(response),
                weborigin=weborigin
            )
        )
    
    def parse(self, response):
        jobcards = response.xpath(self.selectors['link']).getall()
        next_page = response.xpath(self.selectors['next_page']).get()

        for link in jobcards:
            yield response.follow(
                link,
                callback=self.parse_jobpost,
                cb_kwargs=dict(
                    weborigin=self.get_weborigin(response)
                )
            )

        # if next_page:
        #     yield response.follow(
        #         next_page,
        #         callback=self
        #     )

    def validate_company(self, response, company):        
        if not self.is_active:
            return True

        crawled_company = self.get_company(response)

        self.is_active = all([
            company.name == crawled_company['name'],
            company.description == crawled_company['description']
        ])
    
    def validate_jobpost(self, response, jobpost):
        if not self.is_active:
            return True

        crawled_jobpost = self.get_jobpost(response)

        self.is_active = all([
            jobpost.title == crawled_jobpost['title'],
            jobpost.description == crawled_jobpost['description']
        ])

    def validate(self, objects):
        yield scrapy.Request(
            objects['jobpost'].origin_url,
            callback=self.validate_jobpost,
            cb_kwargs=dict(jobpost=objects['jobpost'] )
        )

        yield scrapy.Request(
            objects['company'].origin_url,
            callback=self.validate_company,
            cb_kwargs=dict( company=objects['company'] )
        )
