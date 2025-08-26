from os import environ

from split_settings.tools import include, optional


environ.setdefault("DJANGO_ENV", "development")
_ENV = environ["DJANGO_ENV"]

_base_settings = (
    "components/common.py",
    "components/authentication.py",
    "components/s3_bucket.py",
    "components/celery.py",
    optional("environments/local.py"),
)

include(*_base_settings)
