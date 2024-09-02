from django.urls import path
from . import views

urlpatterns = [
    path('api/apod/', views.apod_view, name='apod_json'),
    path('', views.index_view, name='index'),
    path('planets/', views.planets_view, name='planets'),
    path('api/planet-info/<str:planet_name>/', views.planet_info_view, name='planet_info'),
]