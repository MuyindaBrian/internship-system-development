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
    api.post('/auth/login/', { email, password }).then((response) => response.data),
  register: (email, password, name, passwordConfirm) =>
    api.post('/auth/register/', { email, password, password_confirm: passwordConfirm || password, name }).then((response) => response.data),
  logout: () =>
    api.post('/auth/logout/').then((response) => response.data),
  getCurrentUser: () =>
    api.get('/auth/me/').then((response) => response.data),
};

export const applicationsAPI = {
  getAll: () =>
    api.get('applications/').then((response) => response.data),
  getById: (id) =>
    api.get(`applications/${id}/`).then((response) => response.data),
};

// Internships endpoints
export const internshipsAPI = {
  getAll: () =>
    api.get('internships/').then((response) => response.data),
  getById: (id) =>
    api.get(`internships/${id}/`).then((response) => response.data),
  create: (data) =>
    api.post('internships/', data).then((response) => response.data),
  update: (id, data) =>
    api.put(`internships/${id}/`, data).then((response) => response.data),
  delete: (id) =>
    api.delete(`internships/${id}/`),
  apply: (id) =>
    api.post(`internships/${id}/apply/`).then((response) => response.data),
};

// Maintenance endpoints
export const maintenanceAPI = {
  getAll: () =>
    api.get('maintenance/').then((response) => response.data),
  getById: (id) =>
    api.get(`maintenance/${id}/`).then((response) => response.data),
  create: (data) =>
    api.post('maintenance/', data).then((response) => response.data),
  update: (id, data) =>
    api.put(`maintenance/${id}/`, data).then((response) => response.data),
  delete: (id) =>
    api.delete(`maintenance/${id}/`),
};

export default api;
