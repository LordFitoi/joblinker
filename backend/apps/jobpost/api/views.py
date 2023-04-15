
from collections import OrderedDict

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from backend.apps.jobpost.api.serializers import JobPostSerializer
from backend.apps.jobpost.models import JobPost


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
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


class JobPostViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    pagination_class = StandardResultsSetPagination
    permission_classes = (AllowAny,)
    serializer_class = JobPostSerializer
    queryset = JobPost.objects.all()
    model = JobPost
    search_fields = ("title", "description")


