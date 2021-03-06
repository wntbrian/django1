import django_filters


from .models import Artist, Genre


class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Фильтр")
    class Meta:
        model = Artist
        fields = ['name',]


class GenreFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Фильтр")
    class Meta:
        model = Genre
        fields = ['name',]