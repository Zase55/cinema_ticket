from django.shortcuts import render
from .models import Movie, Hall, Seat

# Create your views here.
def home_request(request):
    movies = Movie.objects.all()
    return render(request, "app/home.html", {'movies':movies})