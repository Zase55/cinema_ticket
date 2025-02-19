from django.shortcuts import render
from bookings.models import Peliculas

# Create your views here.
def home_request(request):
    peliculas = Peliculas.objects.all()
    return render(request, "app/home.html", {'peliculas':peliculas})