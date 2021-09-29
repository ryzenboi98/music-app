from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from music_app import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]