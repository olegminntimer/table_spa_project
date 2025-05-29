import django_filters

from backend.table_api.models import TableData


class RecordFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    quantity = django_filters.NumberFilter()
    quantity_gt = django_filters.NumberFilter(field_name='quantity', lookup_expr='gt')
    quantity_lt = django_filters.NumberFilter(field_name='quantity', lookup_expr='lt')
    distance = django_filters.NumberFilter()
    distance_gt = django_filters.NumberFilter(field_name='distance', lookup_expr='gt')
    distance_lt = django_filters.NumberFilter(field_name='distance', lookup_expr='lt')

    class Meta:
        model = TableData
        fields = []
