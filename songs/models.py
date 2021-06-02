from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
