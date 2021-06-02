from rest_framework.response import Response
from rest_framework import generics
from .models import Song, Artist
from .serializers import SongSerializer, ArtistSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
