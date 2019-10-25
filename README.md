```
git clone https://github.com/katrek/ukrnrg.git
cd ukrnrg
__python manage.py migrate__
**python manage.py runserver** to run Django server
**celery -A monitoring_project worker -B** to run Celery (Celery workers are working on Redis server on Heroku)

After Celery has been running added urls to database are automatically checked for response status codes with an specified interval when adding a URL to monitor system.
```
