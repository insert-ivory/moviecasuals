from django.contrib import admin

from moviecasuals.director.models import Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    pass