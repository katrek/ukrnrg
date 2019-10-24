from celery import shared_task
from celery import Celery
from modules import get_status_code
import time

app = Celery('tasks', broker='redis://localhost:6379/0')





