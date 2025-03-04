from django.db import models
from cinema.constants import FORMAT_CHOICES, AGE_RATING_CHOICES
import uuid

class Hall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(help_text="Total seats.")
    wheelchair_access = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    row = models.CharField(max_length=2)
    number = models.PositiveIntegerField()
    is_accessible = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('hall', 'row', 'number')

    def __str__(self):
        return f"Sala {self.hall.name} - Fila {self.row} Asiento {self.number}"
    

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(blank=True, null=True)
    duration = models.DurationField()
    age_rating = models.CharField(max_length=10,choices=AGE_RATING_CHOICES)
    original_language = models.CharField(max_length=50)
    subtitles_language = models.CharField(max_length=50, blank=True, null=True)
    format = models.CharField( max_length=10, choices=FORMAT_CHOICES )
    release = models.DateField()
    poster = models.URLField()
    
    def __str__(self):
        return self.title