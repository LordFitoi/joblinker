from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapper.spiders.jobpost import JobpostSpider


class Command(BaseCommand):
    help = "Crawl scrapper spider"

    def handle(self, *args, **options):
        settings = get_project_settings()
        settings.setmodule('scrapper.settings', priority='project')
        process = CrawlerProcess(settings)
        process.crawl(JobpostSpider)
        process.start()