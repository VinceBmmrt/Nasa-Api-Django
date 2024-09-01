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
