from rest_framework import serializers
from music_app.models import Song
from music_app.serializers import MusicGenreSerializer, ArtistSerializer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'genre', 'artists']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['genre'] = MusicGenreSerializer(instance.genre).data

        return rep

