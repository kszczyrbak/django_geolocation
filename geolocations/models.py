from django.db import models

# Create your models here.


class GeoData(models.Model):

    ip = models.models.CharField(max_length=20)
    hostname = models.models.CharField(max_length=255)
    continent = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    latitude = models.FloatField()
    longitude = models.FloatField()

    #location_data = models.JSONField()
