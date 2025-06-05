from unittest import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from table_api.models import TableData
from table_api.paginators import TablePagination
from table_api.serializers import TableDataSerializer


class TableDataAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Создание тестовых данных
        TableData.objects.create(
            date="2023-01-01",
            name="Test Item 1",
            quantity=10,
            distance=100
        )
        # Добавьте больше тестовых данных для пагинации и фильтрации

    def test_get_all_items(self):
        url = reverse('tabledata-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_filter_by_name(self):
        url = reverse('tabledata-list')
        response = self.client.get(url, {'name__contains': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data['results']) > 0)

    def test_pagination(self):
        # Создайте достаточно данных для тестирования пагинации
        url = reverse('tabledata-list')
        response = self.client.get(url, {'page_size': 5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)
        self.assertTrue('count' in response.data)

    def test_ordering(self):
        url = reverse('tabledata-list')
        response = self.client.get(url, {'ordering': '-quantity'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        quantities = [item['quantity'] for item in response.data['results']]
        self.assertEqual(quantities, sorted(quantities, reverse=True))

class TableDataSerializerTests(TestCase):
    def test_serializer_data(self):
        data = {
            'date': '2023-01-01',
            'name': 'Test Item',
            'quantity': 10,
            'distance': 100
        }
        serializer = TableDataSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['name'], 'Test Item')

# class TablePaginationTests(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         # Создайте достаточно данных для тестирования пагинации
#
#     def test_pagination(self):
#         request = self.factory.get('/api/items/?page=2&page_size=5')
#         paginator = TablePagination()
#         queryset = TableData.objects.all()
#         result = paginator.paginate_queryset(queryset, request)
#         self.assertEqual(len(result), 5)