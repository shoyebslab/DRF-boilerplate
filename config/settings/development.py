from .base import *

DEBUG = True

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1", "0.0.0.0"])

CORS_ALLOW_ALL_ORIGINS = True

# In development, fallback to SQLite if PostgreSQL is unavailable or if configured
if env.str("DB_ENGINE", default="").endswith("sqlite3"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Django Debug Toolbar (adopted from DRF reference)
try:
    import debug_toolbar  # noqa: F401
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
    INTERNAL_IPS = env.list("INTERNAL_IPS", default=["127.0.0.1", "localhost"])
except ImportError:
    pass

