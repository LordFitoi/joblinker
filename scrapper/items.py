# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobpostItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    company = scrapy.Field()
    origin_url = scrapy.Field()
    origin = scrapy.Field()


class CompanyItem(scrapy.Item):
    name = scrapy.Field()
    origin = scrapy.Field()
    website = scrapy.Field()
    description = scrapy.Field()


class WebOriginItem(scrapy.Item):
    name = scrapy.Field()
    website = scrapy.Field()