from django.shortcuts import render
from django.views.generic import DetailView

from moviecasuals.director.models import Director


def add_director(request):
    return render(request, 'director/add_director.html')


class DirectorDetails(DetailView):
    template_name = 'director/director-main.html'
    model = Director
    pk_url_kwarg = 'director_id'
