import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Dashboard from './pages/Dashboard';
import InternshipList from './pages/InternshipList';
import MaintenanceRequests from './pages/MaintenanceRequests';
import { authAPI } from './services/api';
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    if (token) {
      setIsAuthenticated(true);
      authAPI.getCurrentUser()
        .then((userData) => {
          setUser(userData);
        })
        .catch(() => {
          setIsAuthenticated(false);
          localStorage.removeItem('auth_token');
        });
    }
  }, []);

  const handleLogin = (userData, token) => {
    setIsAuthenticated(true);
    setUser(userData);
    localStorage.setItem('auth_token', token);
  };

  const handleLogout = async () => {
    try {
      await authAPI.logout();
    } catch (err) {
      console.warn('Logout request failed:', err);
    }

    setIsAuthenticated(false);
    setUser(null);
    localStorage.removeItem('auth_token');
  };

  return (
    <BrowserRouter>
      <div className="min-h-screen bg-background">
        <Navbar isAuthenticated={isAuthenticated} user={user} onLogout={handleLogout} />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={isAuthenticated ? <Navigate to="/dashboard" /> : <Login onLogin={handleLogin} />} />
          <Route path="/register" element={isAuthenticated ? <Navigate to="/dashboard" /> : <Register onLogin={handleLogin} />} />
          <Route path="/dashboard" element={isAuthenticated ? <Dashboard user={user} /> : <Navigate to="/login" />} />
          <Route path="/internships" element={<InternshipList />} />
          <Route path="/maintenance" element={isAuthenticated ? <MaintenanceRequests /> : <Navigate to="/login" />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
