from django.urls import path

from moviecasuals.accounts import views

urlpatterns = [
    path('login/', views.MovieUserLoginView.as_view(), name='login'),
    path('logout/', views.MovieUserLogoutView.as_view(), name='logout'),
    path('register/', views.MovieUserRegistrationView.as_view(), name='register'),
]