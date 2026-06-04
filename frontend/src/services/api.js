import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if it exists
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

// Auth endpoints
export const authAPI = {
  login: (email, password) =>
    api.post('/users/login/', { email, password }),
  register: (email, password, name) =>
    api.post('/users/register/', { email, password, name }),
  logout: () =>
    api.post('/users/logout/'),
  getCurrentUser: () =>
    api.get('/users/me/'),
};

// Internships endpoints
export const internshipsAPI = {
  getAll: () =>
    api.get('/internships/'),
  getById: (id) =>
    api.get(`/internships/${id}/`),
  create: (data) =>
    api.post('/internships/', data),
  update: (id, data) =>
    api.put(`/internships/${id}/`, data),
  delete: (id) =>
    api.delete(`/internships/${id}/`),
};

// Maintenance endpoints
export const maintenanceAPI = {
  getAll: () =>
    api.get('/maintenance/'),
  getById: (id) =>
    api.get(`/maintenance/${id}/`),
  create: (data) =>
    api.post('/maintenance/', data),
  update: (id, data) =>
    api.put(`/maintenance/${id}/`, data),
  delete: (id) =>
    api.delete(`/maintenance/${id}/`),
};

export default api;
