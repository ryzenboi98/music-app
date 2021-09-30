from music_app.models import Album
from rest_framework import viewsets, permissions
from music_app import serializers

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all().order_by('created_at')
    serializer_class = serializers.AlbumSerializer
