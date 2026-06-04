# University Internship System

A full-stack web application for managing university internships and maintenance requests using React + Vite for the frontend and Django for the backend.

## Project Structure

```
/
├── frontend/                 # React + Vite frontend application
│   ├── src/
│   │   ├── pages/           # Page components (Home, Login, Register, Dashboard, etc.)
│   │   ├── components/      # Reusable components (Navbar)
│   │   ├── services/        # API service layer
│   │   ├── App.jsx
│   │   ├── index.css        # Tailwind CSS
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
└── backend/                 # Django backend
    ├── internship_system/   # Main Django project settings
    ├── users/               # User authentication app
    ├── internships/         # Internship management app
    ├── maintenance/         # Maintenance request app
    ├── manage.py
    ├── db.sqlite3           # SQLite database
    └── requirements.txt
```

## Features

### Frontend (React + Vite)
- User authentication (Register/Login/Logout)
- Dashboard for viewing internships and maintenance requests
- Internships listing and browsing
- Maintenance request submission and tracking
- Responsive design with Tailwind CSS
- Token-based API authentication

### Backend (Django)
- User management with custom user model
- Token-based authentication
- RESTful API with Django REST Framework
- Internship management with applications
- Maintenance request tracking
- CORS support for frontend communication
- SQLite database

## Tech Stack

### Frontend
- React 19
- Vite 8
- React Router DOM
- Axios
- Tailwind CSS v3

### Backend
- Django 5.x
- Django REST Framework
- Django CORS Headers
- Python 3.x
- SQLite

## Getting Started

### Prerequisites
- Node.js and pnpm
- Python 3.8+

### Frontend Setup

```bash
cd frontend
pnpm install
pnpm dev
```

The frontend will be available at `http://localhost:5173/`

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication
- `POST /api/users/register/` - Register new user
- `POST /api/users/login/` - Login user
- `POST /api/users/logout/` - Logout user
- `GET /api/users/me/` - Get current user info

### Internships
- `GET /api/internships/` - List all internships
- `GET /api/internships/{id}/` - Get internship details
- `POST /api/internships/` - Create internship (admin only)
- `POST /api/internships/{id}/apply/` - Apply for internship
- `PUT /api/internships/{id}/` - Update internship (admin only)
- `DELETE /api/internships/{id}/` - Delete internship (admin only)

### Maintenance
- `GET /api/maintenance/` - List user's maintenance requests
- `GET /api/maintenance/{id}/` - Get maintenance request details
- `POST /api/maintenance/` - Submit maintenance request
- `PUT /api/maintenance/{id}/` - Update maintenance request
- `DELETE /api/maintenance/{id}/` - Delete maintenance request

## Authentication

The application uses token-based authentication. After registering or logging in, the user receives a token that is stored in `localStorage` and sent with each API request in the `Authorization` header as `Token <token>`.

## Development

### Running Both Servers Simultaneously

Terminal 1 (Frontend):
```bash
cd frontend
pnpm dev
```

Terminal 2 (Backend):
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

### Creating Migrations

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
```

### Creating a Superuser

```bash
cd backend
python manage.py createsuperuser
```

Then access admin panel at `http://localhost:8000/admin/`

## Notes

- The frontend automatically connects to the backend at `http://localhost:8000/api`
- Authentication tokens are stored in `localStorage`
- Protected routes automatically redirect unauthenticated users to login
- The application uses CORS to allow cross-origin requests from the frontend

## Future Enhancements

- Add user role-based permissions
- Implement email notifications
- Add file upload support for documents
- Implement advanced search and filtering
- Add analytics dashboard
- Implement real-time updates with WebSockets
