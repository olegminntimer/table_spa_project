#!/bin/sh

# Применяем миграции
python manage.py migrate

# Заполняем базу данных (если она пустая)
python manage.py generate_data

# Запускаем основной процесс (например, Gunicorn для Django)
exec "$@"