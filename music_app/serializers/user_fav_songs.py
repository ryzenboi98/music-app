from rest_framework import serializers
from music_app.models import UserFavoriteSong
from music_app.serializers import MusicGenreSerializer, ArtistSerializer

class UserFavSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavoriteSong
        fields = ['id', 'favourite_songs']
