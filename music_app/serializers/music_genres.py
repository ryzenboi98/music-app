from rest_framework import serializers
from music_app.models import MusicGenre

class MusicGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicGenre
        fields = ['id', 'name']