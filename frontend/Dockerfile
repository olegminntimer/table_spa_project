# Используем официальный образ Node.js
FROM node:18-alpine

# Рабочая директория в контейнере
WORKDIR /app

# Копируем package.json и package-lock.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы проекта
COPY . .

# Запускаем сервер разработки
CMD ["npm", "run", "dev"]

# Открываем порт, который использует Vite (обычно 5173)
EXPOSE 5173