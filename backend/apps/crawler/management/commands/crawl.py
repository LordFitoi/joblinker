from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from backend.apps.jobpost.models import WebsiteOrigin
from backend.apps.crawler.models import CrawlerRecord
from scrapper.spiders.recolector import RecolectorSpider
from scrapper.spiders.validator import ValidatorSpider


class Command(BaseCommand):
    help = "Crawl scrapper spider"

    def handle(self, *args, **options):
        settings = get_project_settings()
        settings.setmodule('scrapper.settings', priority='project')
        
        RecolectorSpider.record = CrawlerRecord.objects.create()
        ValidatorSpider.objects = {
            origin.name: {
                "jobpost": jobpost,
                "company": jobpost.company
            }

            for origin in WebsiteOrigin.objects.all()
            if origin and (jobpost := origin.jobpost_set.first())
        }

        process = CrawlerProcess(settings)
        validation = process.crawl(ValidatorSpider)
        validation.addCallback(lambda _: process.crawl(RecolectorSpider))

        process.start()
