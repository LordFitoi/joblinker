from django.contrib import admin
from .models import Category, Company, JobPost, Location, WebsiteOrigin


@admin.register(WebsiteOrigin)
class WebsiteOriginAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "website", "created_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "website", "created_at")


@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "company", "created_at")
