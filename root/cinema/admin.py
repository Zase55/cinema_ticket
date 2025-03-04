from django.contrib import admin
from cinema.models import Movie

class MoviesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MoviesAdmin)
