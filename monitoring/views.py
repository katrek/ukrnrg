from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import URLMonitor
from django.shortcuts import render
from modules.get_full_class_name import get_full_class_name
from modules.get_status_code import get_status_code
import requests


def IndexView(request):
    urls = URLMonitor.objects.all()
    status_code_list = []
    for i in range(len(urls)):
        try:
            status_code_list.append(get_status_code(url=urls[i]))
        except requests.exceptions.RequestException as e:
            status_code_list.append(get_full_class_name(e))
    info = {k:v for k, v in zip(urls, status_code_list)}
    return render(request, 'index.html', {'info':info})


# class IndexView(ListView):
#     template_name = 'index.html'
#     model = URL_monitor
#     context_object_name = 'urls'

class CreateURL(CreateView):
    template_name = 'create_url.html'
    model = URLMonitor
    fields = ('url', 'interval')


class DeleteURL(DeleteView):
    template_name = 'delete_url.html'
    model = URLMonitor
    context_object_name = 'url'
    success_url = reverse_lazy('index')

