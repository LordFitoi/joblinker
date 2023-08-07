"""
WSGI config for joblinker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.config.production")

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "feline"))

application = get_wsgi_application()
application = WhiteNoise(application, root=str(ROOT_DIR / "staticfiles"))
application.add_files(str(ROOT_DIR / "staticfiles"), prefix="staticfiles/")
