from django.db import models
from rest_framework import serializers
from .models import Song, Artist, Station, DailySchedule, DailyScheduleSong


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = '__all__'


class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'


class DailyScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailySchedule
        fields = '__all__'


class DailyScheduleSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyScheduleSong
        fields = '__all__'

