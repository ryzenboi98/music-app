from rest_framework import serializers
from music_app.models import Album
from .songs import SongSerializer

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    music_genre = serializers.CharField()
    songs = SongSerializer(many=True)
    class Meta:
        model = Album
        fields = ['id', 'name', 'music_genre', 'songs']

    def create(self, validated_data):
        check_music_genres(validated_data)

        return super(AlbumSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        check_music_genres(validated_data)

        instance = super(AlbumSerializer, self).update(instance, validated_data)

        return instance


def check_music_genres(validated_data):
    songs = validated_data['songs']
    music_genre = validated_data['music_genre']

    if music_genre:
        for song in songs:
            if song.genre != music_genre:
                raise serializers.ValidationError("Album genre doesn't match for every song.")