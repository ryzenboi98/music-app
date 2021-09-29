from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from music_app import serializers

# Custom Permissions
class UserReadWritePermission(permissions.BasePermission):
    message = 'User can only see and edit his own information'

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id

# Views
class UserViewSet(viewsets.ModelViewSet, UserReadWritePermission):
    permission_classes = [UserReadWritePermission]

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer