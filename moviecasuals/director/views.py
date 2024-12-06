from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from moviecasuals.director.forms import EditDirectorForm
from moviecasuals.director.models import Director


def add_director(request):
    return render(request, 'director/add_director.html')


class DirectorDetails(DetailView):
    template_name = 'director/director-main.html'
    model = Director
    pk_url_kwarg = 'director_id'


class EditDirectorView(LoginRequiredMixin, UpdateView):
    template_name = 'director/edit_director.html'
    pk_url_kwarg = 'director_id'
    model = Director
    form_class = EditDirectorForm

    def get_success_url(self):
        director_id = self.object.id
        return reverse_lazy('director-details', kwargs={'director_id': director_id})


class DeleteDirectorView(LoginRequiredMixin, DeleteView):
    template_name = 'director/delete_director.html'
    model = Director
    pk_url_kwarg = 'director_id'
    success_url = reverse_lazy('homepage')