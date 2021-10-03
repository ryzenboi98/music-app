import django_filters
from django_filters import rest_framework as filters
from music_app.models import Album


class AlbumFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    songs__name = django_filters.CharFilter(lookup_expr="icontains")


    class Meta:
        model = Album
        fields = ('name', 'songs__name', 'songs__genre__name')