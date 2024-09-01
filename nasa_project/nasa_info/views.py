import requests
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import os

def apod_view(request):
    api_key = settings.NASA_API_KEY
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(data)

def index_view(request):
    html_file_path = os.path.join(settings.BASE_DIR, 'nasa_info/static/index.html')
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    return HttpResponse(html_content)

def planets_view(request):
    html_file_path = os.path.join(settings.BASE_DIR, 'nasa_info/static/planets.html')
    with open(html_file_path, 'r') as file:
        html_content = file.read()
    return HttpResponse(html_content)

def planet_view(request, planet):
    # Example data for planets
    planet_data = {
        "mercury": {"title": "Mercury", "url": "http://example.com/mercury.jpg", "explanation": "Information about Mercury"},
        "venus": {"title": "Venus", "url": "http://example.com/venus.jpg", "explanation": "Information about Venus"},
        "earth": {"title": "Earth", "url": "http://example.com/earth.jpg", "explanation": "Information about Earth"},
        "mars": {"title": "Mars", "url": "http://example.com/mars.jpg", "explanation": "Information about Mars"},
        "jupiter": {"title": "Jupiter", "url": "http://example.com/jupiter.jpg", "explanation": "Information about Jupiter"},
        "saturn": {"title": "Saturn", "url": "http://example.com/saturn.jpg", "explanation": "Information about Saturn"},
        "uranus": {"title": "Uranus", "url": "http://example.com/uranus.jpg", "explanation": "Information about Uranus"},
        "neptune": {"title": "Neptune", "url": "http://example.com/neptune.jpg", "explanation": "Information about Neptune"},
    }

    data = planet_data.get(planet, {"title": "Unknown", "url": "", "explanation": "No information available"})
    return JsonResponse(data)
