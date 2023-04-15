from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend.apps.jobpost.api.views import JobPostViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("jobposts", JobPostViewSet)

app_name = "api"
urlpatterns = router.urls