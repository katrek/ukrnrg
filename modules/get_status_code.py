import requests

def get_status_code(url):
    response = requests.get(url)
    status_code = response.status_code
    return status_code
