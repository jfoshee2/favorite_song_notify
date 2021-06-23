from django.db import models
from django.db.models.fields.related import ManyToManyField, OneToOneField

# Create your models here.

class Station(models.Model):
    name = models.CharField(max_length=200)
    frequency = models.DecimalField(max_digits=5, decimal_places=2)


class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)


class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ManyToOneRel(Artist, to=Artist, field_name="artist")
    genre = models.CharField(max_length=100)
    station = ManyToManyField(Station, verbose_name="list of stations that this song is played on")


class DailySchedule(models.Model):
    station = OneToOneField(Station, verbose_name="Station that the daily schedule is tied to", on_delete=models.CASCADE)
    song = ManyToManyField(Song, verbose_name="list of songs to be played that particular day")


class DailyScheduleSong(models.Model):
    song = OneToOneField(Song, verbose_name="Song to be played at specific time", on_delete=models.CASCADE)
    daily_schedule = OneToOneField(DailySchedule, verbose_name="Corresponding Daily Schedule", on_delete=models.CASCADE)
    date = models.DateTimeField()

