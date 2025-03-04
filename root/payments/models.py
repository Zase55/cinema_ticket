from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=7)
    price = models.FloatField()
    price_id = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name