from django.urls import path

from moviecasuals.movie import views

urlpatterns = [
    path('add-movie/', views.add_movie, name='add-movie'),
]