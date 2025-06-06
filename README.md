# Table SPA Application

SPA-приложение для отображения и управления табличными данными с возможностью сортировки, фильтрации и пагинации.

## Технологии

- **Backend**: Python 3.11, Django 4.2, Django REST Framework, PostgreSQL
- **Frontend**: Svelte, Axios
- **Инфраструктура**: Docker, Nginx

## Структура проекта
    table_spa_project/
    ├── backend/ # Django приложение
    │ ├── config/ # Настройки проекта
    │ ├── table_api/ # Приложение с API
    │ ├── Dockerfile # Конфигурация для бекенда
    │ └── requirements.txt # Зависимости Python
    ├── svelte-front/ # Svelte приложение
    │ ├── src/ # Исходный код фронтенда
    │ ├── Dockerfile # Конфигурация для фронтенда
    │ └── package.json # Зависимости Node.js
    ├── nginx/ # Конфигурация Nginx
    │ ├── nginx.conf # Основной конфиг
    │ └── conf.d/ # Конфиги виртуальных хостов
    ├── docker-compose.yml # Конфигурация Docker
    └── README.md # Этот файл


## Установка и запуск

### Требования

- Docker 20.10+
- Docker Compose 2.0+

### Запуск в development режиме

1. Клонируйте репозиторий:
   ```bash
   https://github.com/olegminntimer/table_spa_project.git
   cd table_spa_project
2. Запустите сервисы:
    ```bash
    docker-compose up --build

3. Приложение будет доступно по адресу:

    Frontend: http://localhost:5173

    Backend API: http://localhost:8000/api
    
    Swagger UI: http://localhost:8000/api/docs

### Запуск в production режиме

1. Создайте файл .env в корне проекта:
    ```txt
    DEBUG=0
    SECRET_KEY=your-secret-key
    ALLOWED_HOSTS=your-domain.com

2. Соберите статические файлы:
    ```bash
    docker-compose exec backend python manage.py collectstatic --noinput
   
3. Перезапустите сервисы:

    ```bash
    docker-compose up -d --build

## API Endpoints

### Таблица данных

- GET /api/items/ - Получить список элементов
    
    Параметры:
- page - номер страницы
- page_size - элементов на странице
- ordering - сортировка (field или -field для DESC)
- Фильтрация: {field}__{lookup}=value (например, name__contains=test)

Пример ответа:

    # json
    {
      "count": 100,
      "next": "http://localhost/api/items/?page=2",
      "previous": null,
      "results": [
        {
          "id": 1,
          "date": "2023-01-01",
          "name": "Item 1",
          "quantity": 10,
          "distance": 15.5
        }
      ]
    }

## Документация API

Доступна через Swagger UI: /api/docs или ReDoc: /api/redoc

### Примеры API запросов

#### Получение данных с фильтрацией
    ```bash
    curl -X GET "http://localhost/api/items/?name__contains=test&quantity__gt=10&ordering=-distance"

## Настройка окружения

Создайте файл .env в папке backend:

    DEBUG=1
    SECRET_KEY=your-secret-key

    SERVER_TYPE=Docker # для реализации приложения с Docker
    # для реализации приложения без Docker: SERVER_TYPE=noDocker

    POSTGRES_DB=your_name_db
    POSTGRES_USER=your_name_user
    POSTGRES_PASSWORD=your_db_password

## Команды для разработки

### Backend

- Применить миграции:
    ```bash
    docker-compose exec backend python manage.py migrate
- Создать суперпользователя:
    ```bash
    docker-compose exec backend python manage.py createsuperuser
- Запустить тесты:
  ```bash
  docker-compose exec backend python manage.py test
  
### Frontend

- Установить зависимости:
    ```bash
    docker-compose exec svelte-front npm install

- Запустить в development режиме:
  ```bash
  docker-compose exec svelte-front npm run dev

## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
