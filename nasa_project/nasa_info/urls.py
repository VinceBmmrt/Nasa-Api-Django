# nasa_info/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apod_view, name='apod'),
]
