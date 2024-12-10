from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from moviecasuals.accounts.models import MovieUserModel
from moviecasuals.mixins import AccessControlMixin
from moviecasuals.movie.forms import CreateMovieForm, EditMovieForm
from moviecasuals.movie.models import Movie, MovieUserChoice
from moviecasuals.movie_choices import MovieUserOptions


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


class MovieDetailsView(DetailView):
    template_name = 'movie/movie_details.html'
    model = Movie
    pk_url_kwarg = 'id'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        movie = self.get_object()

        current_option = None
        if self.request.user.is_authenticated:
            user_option = MovieUserChoice.objects.filter(user=self.request.user, movie=movie).first()
            current_option = user_option.options if user_option else None

        context['status_options'] = MovieUserOptions.choices
        context['current_option'] = current_option

        return context


class UpdateMovieOptionView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, id=kwargs.get('id'))
        option = request.POST.get('option')

        if request.user.is_authenticated:
            user_option, created = MovieUserChoice.objects.get_or_create(user=request.user, movie=movie)
            user_option.options = option
            user_option.save()

        return redirect('homepage')


class YourMovieListView(LoginRequiredMixin, DetailView):
    model = MovieUserModel
    pk_url_kwarg = 'id'
    template_name = 'movie/your_movie_options.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context['status_options'] = MovieUserOptions.choices

        return context


class EditMovieView(LoginRequiredMixin, AccessControlMixin, UpdateView):
    template_name = 'movie/edit_movie.html'
    pk_url_kwarg = 'id'
    model = Movie
    form_class = EditMovieForm

    def get_success_url(self):
        return reverse_lazy('movie-details', kwargs={'id': self.object.id})


class DeleteMovieView(LoginRequiredMixin, AccessControlMixin, DeleteView):
    template_name = 'movie/delete_movie.html'
    model = Movie
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
