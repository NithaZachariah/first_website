from django.db import models

class Perfume(models.Model):
    name = models.CharField(max_length=25)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

