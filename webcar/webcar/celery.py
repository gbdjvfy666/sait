import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcdonalds.settings')

app = Celery('mcdonalds')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

import redis

red = redis.Redis(
    host="redis-19430.c1.asia-northeast1-1.gce.cloud.redislabs.com",
    port="19430",
    password="PVf0IEJPNkiyFqaiIKpHEnVUfpDq9GQw",
)