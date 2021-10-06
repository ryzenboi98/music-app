from django.contrib.auth.models import User
from music_app.models import UserFavoriteSong
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from music_app import serializers as ser

# Custom Permissions
class UserReadWritePermission(permissions.BasePermission):
    message = 'User can only see and edit his own information'

    def has_permission(self, request, view):
        if not request.user.is_authenticated and request.method != 'DELETE':
            return True

        if request.user.is_authenticated and not request.user.is_superuser:
            if request.method == 'PUT':
                return True

        return request.method in permissions.SAFE_METHODS or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id or request.user.is_superuser

# Views
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserReadWritePermission]

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ser.UserSerializer

    @action(detail=True, methods=['get'])
    def favourite_songs(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()

        if not user:
            raise serializers.ValidationError("Not found.")

        user_fav_songs = UserFavoriteSong.objects.filter(user=user)

        serializer = ser.UserFavSongSerializer(user_fav_songs, many=True)

        return Response(serializer.data)
