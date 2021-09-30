import django_filters
from django_filters import rest_framework as filters
from music_app.models import Song

class SongFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Song
        fields = ('name', 'artists', 'genre')