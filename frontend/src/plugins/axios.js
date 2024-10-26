import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://192.168.1.3:5000',
});

// Interceptor para agregar el token
instance.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  console.log('Token:', token); // Verifica si el token se obtiene correctamente
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});

export default instance;
