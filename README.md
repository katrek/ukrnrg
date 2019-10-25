# Test task

* git clone ` https://github.com/katrek/ukrnrg.git `
* cd ukrnrg
* **`pip install -r requirements.txt`**
* **`python manage.py migrate`**
* **`python manage.py runserver`** to run Django server
* **`celery -A monitoring_project worker -B`** to run Celery (Celery workers are working on Redis server on Heroku)

After Celery has been running, added urls are automatically checked for response status codes with an specified interval when adding a URL to monitor system.

