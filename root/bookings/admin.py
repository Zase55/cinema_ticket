from django.contrib import admin
from bookings.models import Peliculas

# Register your models here.
class PeliculasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Peliculas, PeliculasAdmin)