from django.urls import path

from moviecasuals.common import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
]