from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from moviecasuals.accounts.forms import LoginForm, MovieUserRegistrationForm


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