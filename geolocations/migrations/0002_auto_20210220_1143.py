# Generated by Django 3.1.5 on 2021-02-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='continent',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='hostname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='ip',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]