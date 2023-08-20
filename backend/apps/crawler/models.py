from django.db import models
from backend.apps.utils import AbstractBaseModel


class CrawlerRecord(AbstractBaseModel):
    jobposts = models.IntegerField(default=0)
    companies = models.IntegerField(default=0)
