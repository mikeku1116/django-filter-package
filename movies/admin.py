from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year')


admin.site.register(Movie, MovieAdmin)
