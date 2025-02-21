from django.db import models
from django.contrib.auth import get_user_model
from cinema.models import Hall, Seat, Movie
import uuid

User = get_user_model()

class MovieSesion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_session = models.ForeignKey(MovieSesion, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    paid = models.BooleanField(default=False)
