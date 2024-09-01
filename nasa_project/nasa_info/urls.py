from django.urls import path
from . import views

urlpatterns = [
    path('api/apod/', views.apod_view, name='apod_json'),
    path('', views.index_view, name='index'),
]
