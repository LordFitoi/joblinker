from django.contrib import admin
from .models import CrawlerRecord


@admin.register(CrawlerRecord)
class CrawlerRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "jobposts", "companies", "state", "created_at")
