import django_filters
from .models import Hotel

class HotelFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='iexact')
    min_rooms = django_filters.NumberFilter(field_name="number_of_rooms", lookup_expr='gte')
    max_rooms = django_filters.NumberFilter(field_name="number_of_rooms", lookup_expr='lte')

    class Meta:
        model = Hotel
        fields = ['city', 'min_rooms', 'max_rooms']
