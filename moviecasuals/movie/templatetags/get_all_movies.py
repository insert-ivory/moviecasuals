from django import template

from moviecasuals.movie.models import Movie

register = template.Library()
@register.simple_tag
def get_all_movies():
    return Movie.objects.all()