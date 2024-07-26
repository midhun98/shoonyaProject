import django_filters
from .models import Retreat


class RetreatsFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Retreat
        fields = {
        }
