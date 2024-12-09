from django.contrib import admin

from moviecasuals.movie.models import Movie, MovieUserChoice



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(MovieUserChoice)
class MovieAdmin(admin.ModelAdmin):
    pass

