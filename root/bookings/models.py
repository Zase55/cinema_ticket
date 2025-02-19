from django.db import models

# Create your models here.
class Peliculas(models.Model):
    name = models.CharField(max_length=255)
    sala = models.CharField(max_length=255)
    