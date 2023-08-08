import os
from backend.config.settings import * # noqa

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
    "jolinker.site"
]

CSRF_TRUSTED_ORIGINS = [
    "https://joblinker-production.up.railway.app",
    "www.jolinker.site"
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# STORAGE
# ------------------------
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
