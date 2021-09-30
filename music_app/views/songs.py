from music_app.models import Song, Artist, MusicGenre
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from music_app import serializers
from django_filters.rest_framework import DjangoFilterBackend
from music_app import filters

class UserReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser

class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [UserReadOnlyPermissions]

    queryset = Song.objects.all().order_by('created_at')
    serializer_class = serializers.SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.SongFilter

    def create(self, request, *args, **kwargs):
        data = request.data

        music_genre = MusicGenre.objects.get(id=data['genre'])

        new_song = Song.objects.create(name=data["name"], genre=music_genre)
        new_song.save()

        for artist_id in data["artists"]:
            artist_obj = Artist.objects.get(id=artist_id)
            new_song.artists.add(artist_obj)

        serializer = serializers.SongSerializer(new_song)

        return Response(serializer.data)


