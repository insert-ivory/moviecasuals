from django.urls import path

from moviecasuals.movie import views

urlpatterns = [
    path('cereate-movie/', views.CreateMovieView.as_view(), name='create-movie'),
    path('movies-by-genre/<str:genre_choices>/', views.MovieByGenreView.as_view(), name='movies-by-genre'),
]