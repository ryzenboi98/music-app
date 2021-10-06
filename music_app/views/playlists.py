from music_app.models import Playlist
from rest_framework import viewsets, permissions
from music_app import serializers

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = serializers.PlaylistSerializer
