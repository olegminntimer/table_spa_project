from django.db import models
from django.utils import timezone


class TableData(models.Model):
    """Модель для хранения данных таблицы"""

    date = models.DateField(default=timezone.now, verbose_name="Дата")
    name = models.CharField(max_length=255, verbose_name="Название")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    distance = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Расстояние"
    )

    class Meta:
        verbose_name = "Данные таблицы"
        verbose_name_plural = "Данные таблицы"
        ordering = ["date"]

    def __str__(self):
        return f"{self.name} ({self.date})"
