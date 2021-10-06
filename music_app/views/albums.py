from music_app.models import Album
from rest_framework import viewsets, permissions
from music_app import serializers
from django_filters.rest_framework import DjangoFilterBackend
from music_app import filters


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.AlbumFilter
