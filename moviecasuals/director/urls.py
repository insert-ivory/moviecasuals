from django.urls import path

from moviecasuals.director import views

urlpatterns = [
    path('add-director/', views.add_director, name='add-director'),
    path('<int:director_id>/director-details', views.DirectorDetails.as_view(), name='director-details'),
]