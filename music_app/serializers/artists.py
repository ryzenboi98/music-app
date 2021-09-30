from rest_framework import serializers
from music_app.models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']