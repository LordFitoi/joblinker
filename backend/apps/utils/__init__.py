import uuid
from django.conf import settings
from django.db import models
from django.http import HttpResponse

class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def serve_media(_, media_name):
    media_file = open(f"{settings.MEDIA_ROOT}/{media_name}", "rb").read()
    return HttpResponse(media_file, content_type="image")
