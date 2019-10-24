import requests
from monitoring.models import URLMonitor


def get_status_code(url):
    response = requests.get(url)


# def get_status_code(url):
#     response = requests.get(url)
#     status_code = response.status_code
#     return status_code
