from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import URLMonitor
import requests
from .tasks import change_status_code


class IndexView(ListView):
    model = URLMonitor
    template_name = 'index.html'
    context_object_name = 'urls'
    change_status_code.delay()


class CreateURL(CreateView):
    template_name = 'create_url.html'
    model = URLMonitor
    fields = ('url', 'interval')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            self.object.status_code = requests.get(self.object.url)
        except requests.exceptions.RequestException as e:
            self.object.status_code = e
        return super().form_valid(form)


class DeleteURL(DeleteView):
    template_name = 'delete_url.html'
    model = URLMonitor
    context_object_name = 'url'
    success_url = reverse_lazy('index')

class UpdateURL(UpdateView):
    model = URLMonitor

    def form_valid(self, form):
        self.object = form.save(commit=False)

        change_status_code()
