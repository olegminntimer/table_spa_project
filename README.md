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
    ├── frontend/ # Svelte приложение
    │ ├── src/ # Исходный код фронтенда
    │ ├── Dockerfile # Конфигурация для фронтенда
    │ └── package.json # Зависимости Node.js
    ├── nginx/ # Конфигурация Nginx
    │ ├── nginx.conf # Основной конфиг
    │ └── conf.d/ # Конфиги виртуальных хостов
    ├── db_data/ # Данные PostgreSQL
    ├── docker-compose.yml # Конфигурация Docker
    └── README.md # Этот файл


## Установка и запуск

### Требования

- Docker 20.10+
- Docker Compose 2.0+

### Запуск в development режиме

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/table-spa.git
   cd table-spa
2. Запустите сервисы:
    ```bash
    docker-compose up --build

3. Приложение будет доступно по адресу:

    Frontend: http://localhost

    Backend API: http://localhost/api
    
    Swagger UI: http://localhost/api/docs

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

### Деплой на production сервер

1. Скопируйте файлы на сервер:
    ```bash
    scp -r .env docker-compose.yml backend frontend nginx user@server:/path/to/app
2. На сервере:
    ```bash
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build


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
    POSTGRES_DB=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

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
    docker-compose exec frontend npm install

- Запустить в development режиме:
  ```bash
  docker-compose exec frontend npm run dev

## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
