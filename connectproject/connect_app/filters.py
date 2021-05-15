import django_filters as filters
from .models import *

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class EventFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags', lookup_expr='in')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city',required=True)

    class Meta:
        model = Event
        fields = ('tags','name', 'city')
