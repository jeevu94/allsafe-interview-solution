from decouple import config

REDIS_URL = config("REDIS_URL")
REDIS_CELERY_NAMESPACE = config("REDIS_CELERY_NAMESPACE")
REDIS_APP_NAMESPACE = config("REDIS_APP_NAMESPACE")

CELERY_BROKER_URL = f"{REDIS_URL}/{REDIS_CELERY_NAMESPACE}"

CELERYD_TASK_TIME_LIMIT = 300

CELERY_TIMEZONE = "UTC"

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]

CELERYBEAT_SCHEDULE = {
    "update-site-availability-data": {
        "task": "livegraph.tasks.update_site_availability_data",
        "schedule": 1.0,
    },
}
