from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import TableData
from .paginators import TablePagination
from .serializers import TableDataSerializer


class TableDataViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с данными таблицы"""

    queryset = TableData.objects.all()
    serializer_class = TableDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        "name": ["exact", "contains"],
        "quantity": ["exact", "gt", "lt"],
        "distance": ["exact", "gt", "lt"],
    }
    ordering_fields = ["name", "quantity", "distance"]
    ordering = ["-data"]
    pagination_class = TablePagination
