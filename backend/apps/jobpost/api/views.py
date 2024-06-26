from collections import OrderedDict

from rest_framework import filters
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from backend.apps.jobpost.api.serializers import (
    ListCompanySerializer,
    ListJobPostSerializer,
)
from backend.apps.jobpost.models import Company, JobPost


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("total_pages", self.page.paginator.num_pages),
                    ("results", data),
                ]
            )
        )


class BaseListViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
    filter_backends = [filters.SearchFilter]


class JobPostViewSet(BaseListViewSet):
    serializer_class = ListJobPostSerializer
    queryset = JobPost.objects.all()
    model = JobPost
    search_fields = ("title", "description")

    def get_queryset(self):
        queryset = super().get_queryset()

        if company_slug := self.request.query_params.get("company"):
            return queryset.filter(company__slug=company_slug)

        return queryset


class CompanyViewSet(BaseListViewSet):
    serializer_class = ListCompanySerializer
    queryset = Company.objects.all()
    model = Company
    search_fields = ("name", "description", "website")
    lookup_field = "slug"
