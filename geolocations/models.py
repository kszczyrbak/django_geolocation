from django.db import models

# Create your models here.


class Geolocation(models.Model):

    ip = models.CharField(max_length=50, unique=True)
    hostname = models.CharField(max_length=255, blank=True)

    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)

    continent = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)

    #location_data = models.JSONField()
