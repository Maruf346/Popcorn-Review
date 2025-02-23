

# Create your views here.
import requests
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import MovieReview


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

@login_required
def movie_detail(request, movie_id):
    # Fetch movie details from TMDb API
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    movie_response = requests.get(movie_url)

    if movie_response.status_code != 200:
        return render(request, "404.html", {"error": "Movie not found"})

    movie_data = movie_response.json()

    # Handle Review Submission (POST Request)
    if request.method == "POST":
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")

        # Save the user's review
        MovieReview.objects.create(
            movie_id=movie_id,
            user=request.user,
            rating=rating,
            review_text=review_text
        )

        # Redirect to the same page after submission
        return HttpResponseRedirect(request.path)

    # Fetch all reviews and calculate average rating
    reviews = MovieReview.objects.filter(movie_id=movie_id)
    avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]
    avg_rating = round(avg_rating, 1) if avg_rating else "No ratings yet"

    context = {
        "movie": movie_data,
        "reviews": reviews,
        "avg_rating": avg_rating,
    }

    return render(request, "movie_detail.html", context)
