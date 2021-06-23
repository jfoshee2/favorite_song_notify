from django.db.models import query
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Song, Artist, Station, DailySchedule, DailyScheduleSong
from .serializers import SongSerializer, ArtistSerializer, StationSerializer, DailyScheduleSerializer, DailyScheduleSongSerializer


class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistList(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class StationList(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class DailyScheduleList(viewsets.ModelViewSet):
    queryset = DailySchedule.objects.all()
    serializer_class = DailyScheduleSerializer


class DailyScheduleSongList(viewsets.ModelViewSet):
    queryset = DailyScheduleSong.objects.all()
    serializer_class = DailyScheduleSongSerializer

