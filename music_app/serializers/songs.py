from rest_framework import serializers
from music_app.models import Song
from .artists import ArtistSerializer

class SongSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.CharField(max_length=50)
    artists = ArtistSerializer(many=True)

    class Meta:
        model = Song
        fields = ['id', 'name', 'genre', 'artists']
