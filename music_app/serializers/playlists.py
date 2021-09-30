from rest_framework import serializers
from music_app.models import Playlist

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'