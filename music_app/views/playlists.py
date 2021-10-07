from music_app.models import Playlist
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from music_app import serializers
from music_app import filters

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.PlaylistFilter
