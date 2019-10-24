from django.urls import path
from .views import IndexView, CreateURL, DeleteURL

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', CreateURL.as_view(), name='add_url'),
    path('delete/<int:pk>/', DeleteURL.as_view(), name='delete_url')
]



