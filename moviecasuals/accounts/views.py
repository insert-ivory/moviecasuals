from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from moviecasuals.accounts.forms import LoginForm, MovieUserRegistrationForm, MovieUserDetailsForm
from moviecasuals.accounts.models import MovieUserModel
from moviecasuals.mixins import AccessControlMixin


class MovieUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return super().post(request, *args, **kwargs)
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Invalid username or password.')

            return self.form_invalid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class MovieUserLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'accounts/logout.html'

def logout(request):
    return render(request, 'accounts/logout.html')


class MovieUserRegistrationView(CreateView):
    form_class = MovieUserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

class MovieUserDetailsView(DetailView):
    model = MovieUserModel
    template_name = 'accounts/account_details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'movie_user'


class MovieUserEditAccountView(LoginRequiredMixin, AccessControlMixin ,UpdateView):
    template_name = 'accounts/edit_account.html'
    pk_url_kwarg = 'id'
    model = MovieUserModel
    form_class = MovieUserDetailsForm

    def get_user_attribute(self):
        return 'self'

    def get_success_url(self):
        movie_user_id = self.object.id
        print(movie_user_id)
        return reverse_lazy('account-details', kwargs={'id': movie_user_id})



class MovieUserDeleteAccountView(DeleteView):
    template_name = 'accounts/delete_account.html'
    pk_url_kwarg = 'id'
    model = MovieUserModel
    success_url = reverse_lazy('homepage')

    def get_user_attribute(self):
        return 'self'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (obj == request.user or request.user.is_superuser or request.user.is_staff):
            messages.error(request, "You do not have permission to perform this action.")
            return redirect('access-control')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if not (obj == request.user or request.user.is_superuser or request.user.is_staff):
            messages.error(request, "You do not have permission to perform this action.")
            return redirect('access-control')
        return super().post(request, *args, **kwargs)