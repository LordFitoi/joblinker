"""
URL configuration for joblinker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from backend.apps.utils import serve_media, get_robots_txt, show_static_files
from backend.apps.jobpost.views import (
    CompanyDetailView,
    CompanyListView,
    JobpostListView,
)

from backend.apps.jobpost.sitemaps import StaticViewSitemap, CompaniesSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "companies": CompaniesSitemap,
}

urlpatterns = [
    path("", JobpostListView.as_view(), name="jobposts"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("backend.config.api")),
    path("companies/", CompanyListView.as_view(), name="companies"),
    path(
        "companies/<str:company_slug>",
        CompanyDetailView.as_view(),
        name="company-detail",
    ),
    path(
        "privacy/",
        TemplateView.as_view(template_name="privacy/index.html"),
        name="privacy",
    ),
    path(
        "faq/",
        TemplateView.as_view(template_name="faq/index.html"),
        name="privacy",
    ),
    path("users/", include("backend.apps.user.urls")),
    path("accounts/", include("backend.apps.user.auth_urls")),
    path("accounts/", include("allauth.urls")),
    # MISC. URLS
    path("static-files/", show_static_files),
    path(f"{settings.MEDIA_URL[1:]}<str:media_name>", serve_media),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", get_robots_txt),
]
