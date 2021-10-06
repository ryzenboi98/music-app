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

    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.SongFilter
