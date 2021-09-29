from rest_framework import serializers, permissions
from music_app.models import MusicGenre

class MusicGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        permissions_classes = [permissions.IsAdminUser]
        model = MusicGenre
        fields = ['url', 'name']