from music_app.models import Artist
from rest_framework import viewsets, permissions
from music_app import serializers

class UserReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or request.user.is_superuser

class ArtistViewSet(viewsets.ModelViewSet, UserReadOnlyPermissions):
    permission_classes = [UserReadOnlyPermissions]

    queryset = Artist.objects.all().order_by('-created_at')
    serializer_class = serializers.ArtistSerializer
