from django.shortcuts import render
from django.views.generic import ListView

from moviecasuals.movie.models import Movie


def add_movie(request):
    return render(request, 'movie/add_movie.html')


def movie_by_genre(request):
    return render(request, 'movie/movies_by_genre.html')


class MovieByGenreView(ListView):
    template_name = 'movie/movies_by_genre.html'
    context_object_name = 'movies'

    def get_queryset(self):
        genre_choices = self.kwargs['genre_choices']
        return Movie.objects.filter(genre_choices=genre_choices)