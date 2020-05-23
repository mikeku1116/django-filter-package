from django.shortcuts import render
from .models import Movie
from .filters import MovieFilter


def index(request):
    movies = Movie.objects.all()

    movieFilter = MovieFilter(queryset=movies)

    if request.method == "POST":
        movieFilter = MovieFilter(request.POST, queryset=movies)

    context = {
        'movieFilter': movieFilter
    }

    return render(request, 'movies/index.html', context)
