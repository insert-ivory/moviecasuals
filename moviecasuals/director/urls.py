from django.urls import path

from moviecasuals.director import views

urlpatterns = [
    path('create-director/', views.MovieUserCreateDirectorView.as_view(), name='create-director'),
    path('<int:director_id>/director-details', views.DirectorDetails.as_view(), name='director-details'),
    path('<int:director_id>/edit-director', views.EditDirectorView.as_view(), name='edit-director'),
    path('<int:director_id>/delete-director', views.DeleteDirectorView.as_view(), name='delete-director'),
]