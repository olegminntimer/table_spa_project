from rest_framework import serializers
from .models import TableData

class TableDataSerializer(serializers.ModelSerializer):
    """Сериализатор для данных таблицы"""
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = TableData
        fields = ['id', 'date', 'name', 'quantity', 'distance']
        read_only_fields = ['id']
