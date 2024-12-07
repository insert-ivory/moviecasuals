from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from moviecasuals.director.forms import EditDirectorForm, MovieUserCreateDirectorForm
from moviecasuals.director.models import Director
from moviecasuals.mixins import AccessControlMixin


def add_director(request):
    return render(request, 'director/create_director.html')

class MovieUserCreateDirectorView(CreateView):
    form_class = MovieUserCreateDirectorForm
    template_name = 'director/create_director.html'
    model = Director
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if not form.is_valid():
            print(form.errors)
            return self.form_invalid(form)

        form.instance.user = self.request.user
        return super().form_valid(form)


class DirectorDetails(DetailView):
    template_name = 'director/director-main.html'
    model = Director
    pk_url_kwarg = 'director_id'


class EditDirectorView(LoginRequiredMixin, AccessControlMixin, UpdateView):
    template_name = 'director/edit_director.html'
    pk_url_kwarg = 'director_id'
    model = Director
    form_class = EditDirectorForm

    def get_success_url(self):
        director_id = self.object.id
        return reverse_lazy('director-details', kwargs={'director_id': director_id})


class DeleteDirectorView(LoginRequiredMixin, AccessControlMixin, DeleteView):
    template_name = 'director/delete_director.html'
    model = Director
    pk_url_kwarg = 'director_id'
    success_url = reverse_lazy('homepage')

