from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Home page
    path('planets/', views.planets_view, name='planets'),  # Page with planet selector
    path('api/planet/<str:planet>/', views.planet_view, name='planet_data'),  # API endpoint for planet data
    path('api/apod/', views.apod_view, name='apod_json'),  # Existing APOD API
]