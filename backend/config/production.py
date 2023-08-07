from backend.config.settings import * # noqa

DEBUG = False


# SECURITY
# ------------------------------------------------------------------------------ 
CORS_ALLOWED_ORIGINS = []

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = []
ALLOWED_HOSTS = []

ALLOWED_HOSTS = [
    "joblinker-production.up.railway.app",
    "jolinker.com"
]

CSRF_TRUSTED_ORIGINS = [
    "https://joblinker-production.up.railway.app",
    "jolinker.com"
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# STATIC
# ------------------------
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"