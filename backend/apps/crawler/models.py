from django.db import models
from backend.apps.utils import AbstractBaseModel


class CrawlerRecord(AbstractBaseModel):
    class CrawlState(models.TextChoices):
        COMPLETE = "Complete"
        FAILED = "Failed"
        PROCESS = "Process"
    
    jobposts = models.IntegerField(default=0, editable=False)
    companies = models.IntegerField(default=0, editable=False)
    state = models.CharField(
        max_length=20,
        choices=CrawlState.choices,
        default=CrawlState.PROCESS,
    )

    class Meta:
        ordering = ["-created_at"]

    def add_count(self, field_name):
        setattr(self, field_name, getattr(self, field_name) + 1)
        self.save()

    def mark_as_failed(self):
        self.state = self.CrawlState.FAILED
        self.save()
    
    def mark_as_complete(self):
        self.state = self.CrawlState.COMPLETE
        self.save()
