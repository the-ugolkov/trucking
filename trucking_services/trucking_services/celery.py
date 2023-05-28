import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trucking_services.settings')

app = Celery('trucking_services')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_location_every_3_min': {
        'task': 'finder.tasks.update_cars_location',
        'schedule': crontab(minute='*/3'),
    },
}