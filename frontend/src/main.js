import axios from 'axios';
import App from './App.svelte';

// Базовый URL для API (будет меняться в зависимости от среды)
axios.defaults.baseURL = import.meta.env.DEV
  ? 'http://localhost:8000/api'
  : '/api';

// Интерцептор для обработки ошибок
axios.interceptors.response.use(
  response => response,
  error => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

const app = new App({
  target: document.getElementById('app')
});

export default app;