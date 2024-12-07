from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from moviecasuals.movie.forms import CreateMovieForm
from moviecasuals.movie.models import Movie


class CreateMovieView(CreateView):
    template_name = 'movie/create_movie.html'
    model = Movie
    form_class = CreateMovieForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if not form.is_valid():
            print(form.errors)
            return self.form_invalid(form)

        form.instance.user = self.request.user
        return super().form_valid(form)


class MovieByGenreView(ListView):
    template_name = 'movie/movies_by_genre.html'
    context_object_name = 'movies'

    def get_queryset(self):
        genre_choices = self.kwargs['genre_choices']
        return Movie.objects.filter(genre_choices=genre_choices)