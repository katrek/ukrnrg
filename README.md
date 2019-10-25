# Test task

* git clone ` https://github.com/katrek/ukrnrg.git `
* cd ukrnrg
* **`pip install -r requirements.txt`**
* **`python manage.py migrate`**
* **`python manage.py runserver`** to run Django server
* **`celery -A monitoring_project worker -B`** to run Celery (Celery workers are working on Redis server on Heroku)

After Celery has been running, added urls are automatically checked for response status codes with an specified interval when adding a URL to monitor system.

## Usage overview
* After running Django server, login to the website and add URLs to be checked.
* After URLs added, type **`celery -A monitoring_project worker -B`** in terminal to run Celery workers to work and update connections to these URLs.
* Now you can refresh your page and check, when last connections were made, they will automatically updated every time of interval.
