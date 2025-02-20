

# Create your views here.
import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render


TMDB_API_KEY = "5c479c251bf591218affcb56eea2816d"

def search_movie(request):
    query = request.GET.get("query", "")
    if not query:
        return JsonResponse({"error": "No search query provided"}, status=400)

    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={query}"
    response = requests.get(url)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse({"error": "Movie not found"}, status=404)


def search_page(request):
    return render(request, "search.html")

