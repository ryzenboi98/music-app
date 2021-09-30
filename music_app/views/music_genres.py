from music_app.models import MusicGenre
from rest_framework import viewsets, permissions
from music_app import serializers

class UserReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser

class MusicGenreViewSet(viewsets.ModelViewSet):
    permission_classes = [UserReadOnlyPermissions]

    queryset = MusicGenre.objects.all().order_by('created_at')
    serializer_class = serializers.MusicGenreSerializer
