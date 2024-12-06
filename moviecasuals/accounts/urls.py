from django.urls import path

from moviecasuals.accounts import views

urlpatterns = [
    path('login/', views.MovieUserLoginView.as_view(), name='login'),
    path('confirm-logout/', views.logout, name='logout-confirm'),
    path('logout/', views.MovieUserLogoutView.as_view(), name='logout'),
    path('register/', views.MovieUserRegistrationView.as_view(), name='register'),
    path('<int:id>/details/', views.MovieUserDetailsView.as_view(), name='account-details'),
    path('<int:id>/edit/', views.MovieUserEditAccountView.as_view(), name='edit-account'),
    path('<int:id>/delete/', views.MovieUserDeleteAccountView.as_view(), name='delete-account'),
]