# backend/table_api/management/commands/generate_data.py
import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

from table_api.models import TableData


class Command(BaseCommand):
    help = "Generates random records for the database"

    def handle(self, *args, **options):
        fake = Faker("ru-RU")
        # # Удаляем только если таблица существует
        # if TableData.objects.exists():
        #     TableData.objects.all().delete()

        # Проверяем, есть ли уже данные в базе
        if TableData.objects.exists():
            self.stdout.write(
                self.style.WARNING("Data already exists. Skipping generation.")
            )
            return

        # Генерируем тестовые данные
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2025, 1, 1)
        for _ in range(100):
            random_date = start_date + timedelta(
                days=random.randint(0, (end_date - start_date).days)
            )
            TableData.objects.create(
                date=random_date,
                name=fake.word().capitalize(),
                quantity=random.randint(1, 1000),
                distance=random.uniform(1.0, 1000.0),
            )

        self.stdout.write(self.style.SUCCESS("Successfully generated records"))
