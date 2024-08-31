import requests
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseServerError
from requests.exceptions import RequestException

def apod_view(request):
    api_key = settings.NASA_API_KEY  # Récupère la clé API du fichier settings
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    
    try:
        # Utilisation d'une session pour réutiliser les connexions
        with requests.Session() as session:
            response = session.get(url)
            response.raise_for_status()  # Lève une exception pour les réponses HTTP d'erreur

        data = response.json()

        # Vérifie si les clés attendues sont présentes
        title = data.get('title', 'No Title Available')
        explanation = data.get('explanation', 'No Explanation Available')
        image_url = data.get('url', '')

        context = {
            'title': title,
            'explanation': explanation,
            'image_url': image_url
        }
        
        return render(request, 'nasa_info/apod.html', context)
    
    except RequestException as e:
        # En cas d'erreur de requête, renvoie une page d'erreur serveur
        print(f"Error fetching data from NASA API: {e}")
        return HttpResponseServerError("Error fetching data from NASA API.")
    
    except ValueError as e:
        # En cas d'erreur JSON, renvoie une page d'erreur serveur
        print(f"Error processing JSON data: {e}")
        return HttpResponseServerError("Error processing data from NASA API.")
