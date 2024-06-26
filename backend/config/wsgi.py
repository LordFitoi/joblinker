"""
WSGI config for joblinker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.production")

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
application.add_files(settings.STATIC_ROOT, prefix="staticfiles/")
