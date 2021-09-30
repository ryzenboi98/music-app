from rest_framework import serializers
from music_app.models import MusicGenre

class MusicGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MusicGenre
        fields = ['url', 'name']