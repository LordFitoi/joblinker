from os import environ
from backend.config.wsgi import * # noqa

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = []
ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app'
]

DEBUG = False