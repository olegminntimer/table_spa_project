from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import TableData
from .paginators import TablePagination
from .serializers import TableDataSerializer


class TableDataViewSet(viewsets.ModelViewSet):
    """ViewSet для работы с данными таблицы"""
    queryset = TableData.objects.all()
    serializer_class = TableDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'name': ['exact', 'contains'],
        'quantity': ['exact', 'gt', 'lt'],
        'distance': ['exact', 'gt', 'lt'],
    }
    ordering_fields = ['name', 'quantity', 'distance']
    ordering = ['-id']
    pagination_class = TablePagination

    # @action(detail=False, methods=['post'])
    # def generate_data(self, request):
    #     """Эндпоинт для генерации тестовых данных"""
    #     count = request.data.get('count', 100)
    #     message = TableData.generate_random_data(count)
    #     return Response({'status': 'success', 'message': message})
