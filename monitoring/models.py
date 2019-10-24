from django.db import models
from django.urls import reverse


INTERVAL_CHOICES = [
    (30, '30 seconds'),
    (60, '60 seconds'),
]


class URLMonitor(models.Model):
    url = models.TextField(unique=True, verbose_name='URL')
    interval = models.IntegerField(choices=INTERVAL_CHOICES, verbose_name='Refresh interval in seconds')
    last_checked = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('index')

