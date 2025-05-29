from django.db import models
from django.utils import timezone
from faker import Faker
import random

class TableData(models.Model):
    """Модель для хранения данных таблицы"""
    date = models.DateField(default=timezone.now, verbose_name="Дата")
    name = models.CharField(max_length=255, verbose_name="Название")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Расстояние")

    class Meta:
        verbose_name = "Данные таблицы"
        verbose_name_plural = "Данные таблицы"
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} ({self.date})"

    @classmethod
    def generate_random_data(cls, count=100):
        """Метод для генерации тестовых данных"""
        objects = []
        fake = Faker()

        for i in range(count):
            objects.append(cls(
                name=fake.word().capitalize(),
                quantity=random.randint(1, 1000),
                distance=random.uniform(1.0, 1000.0)
            ))
        cls.objects.bulk_create(objects)
        return f"Создано {count} тестовых записей"
