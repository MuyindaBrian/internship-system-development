# University Internship System - Backend

A comprehensive Django REST Framework backend for managing university internship allocations, maintenance requests, and administrative inquiries.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Populate sample data
python manage.py populate_db

# Start server
python manage.py runserver
```

Access the API at: `http://localhost:8000/api/`
Admin panel: `http://localhost:8000/admin/`

## Features

### 🔐 User Management
- **Token-based authentication** for secure API access
- **Role-based access control**: Student, Admin, Company
- User registration, login, and profile management
- Password security and validation

### 📚 Internship Management
- **Create, read, update, delete** internships
- **Search and filter** by company, status, and title
- **Track applications** from students
- **Pagination** support for large datasets
- Status management (active, closed, pending)

### 🔧 Maintenance Requests
- **Submit maintenance requests** for facilities
- **Track status** throughout resolution process
- **Admin assignment** and management
- **Search and filter** capabilities
- Pagination support

### 📝 AOB (Any Other Business) System
- **Submit general inquiries** and concerns
- **Categorization**: Payment, Allocation, Support, Other
- **Admin review workflow** with approval/rejection
- **Response tracking** and resolution
- Status progression: pending → in_review → approved/rejected → resolved

### 👥 Admin Dashboard
- Manage users and their roles
- Approve/reject applications
- Handle maintenance requests
- Review and respond to AOB requests
- Access comprehensive admin interface

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/me/` - Get current user info

### Internships
- `GET /api/internships/` - List all internships
- `POST /api/internships/` - Create internship (Admin)
- `GET /api/internships/{id}/` - Get internship details
- `PUT /api/internships/{id}/` - Update internship
- `DELETE /api/internships/{id}/` - Delete internship
- `POST /api/internships/{id}/apply/` - Apply for internship

### Applications
- `GET /api/applications/` - List user's applications
- `GET /api/applications/{id}/` - Get application details

### Maintenance
- `GET /api/maintenance/` - List maintenance requests
- `POST /api/maintenance/` - Create request
- `GET /api/maintenance/{id}/` - Get details
- `PUT /api/maintenance/{id}/` - Update request
- `DELETE /api/maintenance/{id}/` - Delete request

### AOB
- `GET /api/aob/` - List AOB requests
- `POST /api/aob/` - Create request
- `GET /api/aob/{id}/` - Get details
- `POST /api/aob/{id}/approve/` - Approve (Admin)
- `POST /api/aob/{id}/reject/` - Reject (Admin)
- `POST /api/aob/{id}/resolve/` - Resolve (Admin)

## Test Credentials

After running `python manage.py populate_db`:

- **Admin**: admin@example.com / admin123
- **Student**: student1@university.edu / student123
- **Company**: company1@techcorp.com / company123

## Technology Stack

- **Django 6.0.6** - Web framework
- **Django REST Framework 3.14.0** - API development
- **django-cors-headers 4.3.1** - CORS support
- **SQLite/PostgreSQL** - Database
- **Token Authentication** - Security

## Directory Structure

```
backend/
├── aob/                          # Any Other Business app
├── internships/                  # Internship management app
│   └── management/commands/
│       └── populate_db.py        # Sample data generator
├── maintenance/                  # Maintenance requests app
├── users/                        # User authentication app
├── internship_system/            # Project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL routing
│   ├── permissions.py           # Custom permissions
│   └── wsgi.py                  # WSGI configuration
├── manage.py                     # Django management
├── db.sqlite3                    # SQLite database
├── requirements.txt              # Python dependencies
├── API_DOCUMENTATION.md          # Complete API docs
└── SETUP_GUIDE.md               # Detailed setup guide
```

## Database Models

### CustomUser
Enhanced Django user with role-based access control
- Fields: email, name, user_type, phone, bio, company_name

### Internship
Internship listings created by admins
- Fields: title, description, company, duration, status, created_by

### InternshipApplication
Student applications for internships
- Fields: internship, applicant, status, applied_at

### MaintenanceRequest
Facility maintenance requests from users
- Fields: room, issue, status, requested_by, resolved_at

### AOBRequest
General inquiry system for students
- Fields: title, description, category, status, submitted_by, reviewed_by, response

## Configuration

### CORS Settings
Update `internship_system/settings.py` to include your frontend URL:
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',     # React dev server
    'http://localhost:3000',     # Alternative port
    'https://yourdomain.com',    # Production
]
```

### Database
Default: SQLite (db.sqlite3)
Production: PostgreSQL recommended

This backend already supports `DATABASE_URL` environment configuration, and it can connect to a Supabase hosted PostgreSQL database.

For Supabase, use the project database connection string in your backend `.env` file:
```env
DATABASE_URL=postgres://postgres:<password>@db.<project>.supabase.co:5432/postgres
```

If you are not using Supabase database hosting, you can still use PostgreSQL with settings like:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'internship_system',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

> Note: Supabase provides hosted Postgres and Auth, but it does not host Django apps directly. The Django API must still be deployed to a Python-compatible host, while using Supabase as the database layer. Recommended hosts include Render, Railway, Fly.io, or any Docker-compatible provider.

## Development

### Run Development Server
```bash
python manage.py runserver
```

### Make Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Access Admin Panel
Navigate to: `http://localhost:8000/admin/`

### Run Tests
```bash
python manage.py test
```

## Production Deployment

### Using Gunicorn
```bash
pip install gunicorn
gunicorn internship_system.wsgi:application --bind 0.0.0.0:8000
```

### Using Docker
```bash
docker build -t internship-backend .
docker run -p 8000:8000 internship-backend
```

### Docker Compose
```bash
docker compose up --build
```

The backend includes `docker-compose.yml` for a local Postgres + Django setup.

### Deploying on Vercel
The backend is ready for a Vercel Docker deployment from the `backend/` directory.
Use `backend/vercel.json`, `backend/Dockerfile`, and `backend/.dockerignore`.
If you deploy from Vercel, set the project root to `backend/` and configure environment variables there.

For full instructions, see `DEPLOYMENT_DOCKER_VERCEL.md`.

### Security Checklist
- [ ] Set DEBUG = False
- [ ] Use environment variables for secrets
- [ ] Configure HTTPS/SSL
- [ ] Set secure ALLOWED_HOSTS
- [ ] Configure PostgreSQL database
- [ ] Set up proper CORS origins
- [ ] Enable CSRF protection
- [ ] Use production WSGI server

## Documentation

- **API_DOCUMENTATION.md** - Complete API reference with examples
- **SETUP_GUIDE.md** - Detailed installation and configuration guide
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Support & Troubleshooting

### Common Issues

**ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**Migration Errors**
```bash
python manage.py migrate --fake
python manage.py migrate
```

**Database Reset (Development Only)**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py populate_db
```

## License

This project is part of a university coursework assignment.

## Author

Developed as part of Full-Stack Web System Development coursework.

---

**Version**: 1.0  
**Last Updated**: June 4, 2026  
**Status**: Production Ready ✅
