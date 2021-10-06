from rest_framework import serializers
from music_app.models import Album
from music_app.serializers import MusicGenreSerializer

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'music_genre', 'songs']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['music_genre'] = MusicGenreSerializer(instance.music_genre).data

        return rep

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
        all_genres_equal = all(song.genre == music_genre for song in songs)

        if not all_genres_equal:
            raise serializers.ValidationError("Album genre doesn't match for every song.")