import requests

from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import URLMonitor
from .tasks import change_status_code

from modules.get_full_class_name import get_full_class_name


class IndexView(ListView):
    model = URLMonitor
    template_name = 'index.html'
    context_object_name = 'urls'
    change_status_code.delay()


class CreateURL(LoginRequiredMixin, CreateView):
    template_name = 'create_url.html'
    model = URLMonitor
    fields = ('url', 'interval')
    login_url = 'login'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        try:
            self.object.status_code = requests.get(self.object.url)
        except requests.exceptions.RequestException as e:
            self.object.status_code = get_full_class_name(e)
        return super().form_valid(form)


class DeleteURL(LoginRequiredMixin, DeleteView):
    template_name = 'delete_url.html'
    model = URLMonitor
    context_object_name = 'url'
    success_url = reverse_lazy('index')
    login_url = 'login'

