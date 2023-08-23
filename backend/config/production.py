import logging
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from backend.config.settings import *  # noqa


DEBUG = False

# DATABASE
# ------------------------------------------------------------------------------
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = os.environ.get("CONN_MAX_AGE", 60)

# SECURITY
# ------------------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = []
CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = [
    "joblinker-production.up.railway.app",
    "www.joblinker.site",
    "joblinker.site",
]

CSRF_TRUSTED_ORIGINS = [
    "https://joblinker-production.up.railway.app",
    "www.joblinker.site",
    "joblinker.site",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# SENTRY
# ------------------------

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[
        LoggingIntegration(
            level=logging.INFO,  # Capture info and above as breadcrumbs
            event_level=logging.ERROR,  # Send errors as events
        ),
        DjangoIntegration(),
    ],
    environment=os.environ.get("SENTRY_ENVIRONMENT", "production"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
