from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task
from .models import URLMonitor
import requests
import datetime


@periodic_task(name='UPDATE_STATUS_CODE', run_every=datetime.timedelta(seconds=10))
def change_status_code():
    while True:
        model_ids = URLMonitor.objects.all().values_list('id', flat=True)
        for id in model_ids:
            objects = URLMonitor.objects.get(pk=id)
            response = requests.get(objects.url)
            status_code = response.status_code
            URLMonitor.objects.filter(pk=id).update(
                status_code=status_code,
                last_checked = str(datetime.datetime.now())
            )
        return None




