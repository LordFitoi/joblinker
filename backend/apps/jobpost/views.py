from typing import Any, Dict
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector
from datetime import datetime, timedelta
from .models import Company, JobPost


class JobpostListView(ListView):
    template_name = "index.html"
    model = JobPost
    paginate_by = 10
    search_fields = ("title", "description", "origin_url", "job_type")

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        if search_query := self.request.GET.get("search"):
            search_vector = queryset.annotate(search=SearchVector(*self.search_fields))
            queryset = search_vector.filter(search=search_query)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_count"] = self.get_queryset().count()

        return context


class CompanyListView(ListView):
    template_name = "companies/index.html"
    model = Company
    paginate_by = 10
    search_fields = ("description", "name", "website", "origin_url")

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        if search_query := self.request.GET.get("search"):
            search_vector = queryset.annotate(search=SearchVector(*self.search_fields))
            queryset = search_vector.filter(search=search_query)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_count"] = self.get_queryset().count()

        return context


class CompanyDetailView(ListView):
    template_name = "companies/details/index.html"
    model = JobPost
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)

        return queryset.filter(company__slug=self.kwargs["company_slug"])

    def get_object(self):
        return Company.objects.filter(slug=self.kwargs["company_slug"]).first()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()

        return context
