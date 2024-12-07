from django import template

from moviecasuals.movie.models import Movie

register = template.Library()


@register.simple_tag
def get_unique_movie_genres():
    return Movie.objects.values('genre_choices').distinct()

