import requests
import datetime

from django.utils import timezone

from celery.task import periodic_task
from .models import URLMonitor

from modules.get_full_class_name import get_full_class_name


intervals = URLMonitor.objects.all().values_list('interval', flat=True)
# Preventing the exceptions when DB is empty
if intervals:
    seconds = intervals[0]
else:
    seconds = 10

@periodic_task(name='UPDATE_STATUS_CODE',
               run_every=datetime.timedelta(seconds=seconds))
def change_status_code():
    while True:
        model_ids = URLMonitor.objects.all().values_list('id', flat=True)
        for id in model_ids:
            objects = URLMonitor.objects.get(pk=id)
            try:
                status_code = requests.get(objects.url)
            except Exception as e:
                status_code = get_full_class_name(e)
            URLMonitor.objects.filter(pk=id).update(
                status_code=status_code,
                last_checked = str(timezone.now())
            )
        return None

