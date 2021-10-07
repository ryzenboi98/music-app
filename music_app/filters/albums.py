import django_filters
from django_filters import rest_framework as filters
from music_app.models import Album


class AlbumFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    music_genre = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Album
        fields = ('name', 'songs__name','music_genre')