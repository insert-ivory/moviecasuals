from django.contrib import admin

from moviecasuals.movie.models import Movie, MovieUserChoice



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'genre_choices', 'approved', 'average_rating')
    search_fields = ('title', 'director__name', 'genre_choices')
    list_filter = ('genre_choices', 'approved', 'director')
    list_editable = ('approved',)
    fields = ('title', 'director', 'genre_choices', 'description', 'picture_url', 'approved')
    actions = ['mark_as_approved']

    def mark_as_approved(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected movies have been marked as approved.")

    mark_as_approved.short_description = "Mark selected movies as approved"


@admin.register(MovieUserChoice)
class MovieAdmin(admin.ModelAdmin):

    list_display = ('user', 'movie', 'options')
    search_fields = ('user__username', 'movie__title', 'options')
    list_filter = ('options', 'movie__genre_choices')
    fields = ('user', 'movie', 'options')
    readonly_fields = ('user', 'movie')

