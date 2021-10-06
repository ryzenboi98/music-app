from music_app.models import UserFavoriteSong, Song
from rest_framework import status, serializers, viewsets, permissions
from rest_framework.response import Response
from music_app import serializers as ser
from django.http import Http404

class UserReadWritePermission(permissions.BasePermission):
    message = 'User can only see and edit his own information'

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser

class UserFavSongViewSet(viewsets.ModelViewSet):
    permission_classes = [UserReadWritePermission]

    queryset = UserFavoriteSong.objects.all()
    serializer_class = ser.UserFavSongSerializer

    def list(self, request):
        user = request.user

        if not user.is_authenticated:
            raise serializers.ValidationError("You can't access this endpoint.")

        user_fav_songs = UserFavoriteSong.objects.filter(user=user)

        serializer = ser.UserFavSongSerializer(user_fav_songs, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
