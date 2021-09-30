from music_app.models import Playlist
from rest_framework import viewsets, permissions
from music_app import serializers

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all().order_by('created_at')
    serializer_class = serializers.PlaylistSerializer
