import uuid, os
from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound

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
        return HttpResponse(media_file, content_type="image")
    
    return HttpResponseNotFound()
