from django.urls import path

from moviecasuals.director import views

urlpatterns = [
    path('add-director/', views.add_director, name='add-director'),
]