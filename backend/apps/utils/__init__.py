import uuid, os
from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.staticfiles import finders


class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def serve_media(_, media_name):
    path = f"{settings.MEDIA_ROOT}/{media_name}"

    if os.path.exists(path):
        media_file = open(path, "rb").read()
        return HttpResponse(media_file, content_type=["image/jpg", "image/png"])

    return HttpResponseNotFound()


def serve_file(filename, content_type):
    try:
        path = finders.find(filename)
        sitemap = open(path, "rb").read()
        return HttpResponse(sitemap, content_type=content_type)

    except FileNotFoundError:
        return HttpResponseNotFound()


def get_robots_txt(_):
    return serve_file("robots.txt", "text/plain")
