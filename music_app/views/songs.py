from music_app.models import Song
from rest_framework import viewsets, permissions
from music_app import serializers

class UserReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser

class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [UserReadOnlyPermissions]

    queryset = Song.objects.all().order_by('-created_at')
    serializer_class = serializers.SongSerializer
