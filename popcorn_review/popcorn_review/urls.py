"""
URL configuration for popcorn_review project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reviews.views import search_movie, search_page, movie_detail, vote_review, home_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', search_movie, name='search_movie'),
    path('search/', search_page, name='search_page'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),  # New route for movie details
    path('api/vote/<int:review_id>/<str:vote_type>/', vote_review, name='vote_review'),
    path('', home_page, name='home_page'),  # Add this for the homepage
]
