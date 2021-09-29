from music_app.models import MusicGenre
from rest_framework import viewsets, permissions
from music_app import serializers

class MusicGenreViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]

    queryset = MusicGenre.objects.all().order_by('-created_at')
    serializer_class = serializers.MusicGenreSerializer
