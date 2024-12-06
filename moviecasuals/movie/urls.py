from django.urls import path

from moviecasuals.movie import views

urlpatterns = [
    path('add-movie/', views.add_movie, name='add-movie'),
    path('movies-by-genre/<str:genre_choices>/', views.MovieByGenreView.as_view(), name='movies-by-genre'),
]