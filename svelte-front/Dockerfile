# Используем официальный образ Node.js
FROM node:18-alpine

# Установка зависимостей, включая Python и build tools
RUN apk add --no-cache python3 py3-pip make g++

# Рабочая директория в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы проекта
COPY . .

# Открываем порт, который использует Vite (обычно 5173)
EXPOSE 5173

# Запускаем сервер разработки
CMD ["npm", "run", "dev"]