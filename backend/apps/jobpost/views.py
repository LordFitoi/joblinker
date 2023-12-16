from typing import Any, Dict
from django.views.generic import ListView
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.contrib.postgres.search import SearchVector
from django.db.models import Count, Q
from .models import Company, JobPost


class JobpostListView(ListView):
    template_name = "index.html"
    model = JobPost
    paginate_by = 20
    search_fields = ("title", "description", "origin_url", "job_type")

    def sorted_by_skills(self, queryset, user):
        query = Count("categories", filter=Q(categories__in=user.profile.skills.all()))
        return queryset.annotate(common_skills=query).order_by(
            "-release_date", "-created_at", "-common_skills"
        )

    def get_date_limit(self):
        midnight_date = datetime.combine(date.today(), datetime.min.time())
        return midnight_date + relativedelta(months=-3)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(created_at__gte=self.get_date_limit())

        if search_query := self.request.GET.get("search"):
            queryset = queryset.annotate(search=SearchVector(*self.search_fields))
            queryset = queryset.filter(search=search_query)

        if self.request.user.is_authenticated:
            queryset = self.sorted_by_skills(queryset, self.request.user)

        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["object_count"] = self.get_queryset().count()

        return context


class CompanyListView(ListView):
    template_name = "companies/index.html"
    model = Company
    paginate_by = 20
    search_fields = ("name", "description", "origin_url", "website")

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.exclude(
            Q(description__isnull=True)
            | Q(description__exact="")
            | Q(jobpost__isnull=True)
        )

        if search_query := self.request.GET.get("search"):
            queryset = queryset.annotate(search=SearchVector(*self.search_fields))
            queryset = queryset.filter(search=search_query)

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
