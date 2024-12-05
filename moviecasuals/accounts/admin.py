from django.contrib import admin

from moviecasuals.accounts.models import MovieUserModel


@admin.register(MovieUserModel)
class MovieUserModelAdmin(admin.ModelAdmin):
    pass