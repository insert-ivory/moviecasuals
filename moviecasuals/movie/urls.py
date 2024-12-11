from django.urls import path

from moviecasuals.movie import views

urlpatterns = [
    path('cereate-movie/', views.CreateMovieView.as_view(), name='create-movie'),
    path('movies-by-genre/<str:genre_choices>/', views.MovieByGenreView.as_view(), name='movies-by-genre'),
    path('<int:id>/movie-details/', views.MovieDetailsView.as_view(), name='movie-details'),
    path('<int:id>/change_option/', views.UpdateMovieOptionView.as_view(), name='movie-option'),
    path('<int:id>/edit-movie/', views.EditMovieView.as_view(), name='movie-edit'),
    path('<int:id>/delete-movie/', views.DeleteMovieView.as_view(), name='movie-delete'),

] + [
    path('api/', views.MovieApiView.as_view(), name='movie-api')
]