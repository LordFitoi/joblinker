from django.db import models
from backend.apps.utils import AbstractBaseModel


class CrawlerRecord(AbstractBaseModel):
    jobposts = models.IntegerField(default=0, editable=False)
    companies = models.IntegerField(default=0, editable=False)

    def add_count(self, field_name):
        setattr(self, field_name, getattr(self, field_name) + 1)
        self.save()
