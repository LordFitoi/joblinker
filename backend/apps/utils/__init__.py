import uuid, os, json
from django.conf import settings
from django.db import models
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import user_passes_test


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


def get_directory_tree(path):
    tree = {"files": []}

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            tree["files"].append(file)

        elif os.path.isdir(os.path.join(path, file)):
            tree[file] = get_directory_tree(os.path.join(path, file))

    return tree


@user_passes_test(lambda u: u.is_staff)
def show_static_files(_):
    static_files = json.dumps(get_directory_tree(settings.STATIC_ROOT), indent=4)

    return HttpResponse(static_files, content_type="application/json")
