from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.shortcuts import reverse
from backend.apps.jobpost.models import Company


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["companies", "jobposts", "privacy"]

    def location(self, item):
        return reverse(item)


class CompaniesSitemap(Sitemap):
    def items(self):
        return Company.objects.all()

    def location(self, item):
        return reverse("company-detail", kwargs={"company_slug": item.slug})

    def lastmod(self, item):
        return item.updated_at
