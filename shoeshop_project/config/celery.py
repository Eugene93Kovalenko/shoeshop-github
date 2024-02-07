from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.update(
    broker_connection_retry_on_startup=True,
    broker_transport_options={"visibility_timeout": 1800},
)
app.autodiscover_tasks()
# TODO
app.conf.beat_schedule = {
    'name': {
        'task': 'analytic.tasks.get_analytic_from_hh_api',
        'schedule': crontab(minute='0', hour='3'),
    }
}
