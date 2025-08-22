from celery.schedules import crontab


CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"

CELERY_TIMEZONE = "UTC"

CELERY_BEAT_SCHEDULE = {}
