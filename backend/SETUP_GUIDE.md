# Django Backend Setup and Deployment Guide

## Project Overview

This is the backend API for the University Internship System, built with Django REST Framework. It provides RESTful API endpoints for managing internships, user authentication, maintenance requests, and general inquiries (AOB).

## System Architecture

### Technology Stack
- **Framework**: Django 6.0.6
- **API**: Django REST Framework 3.14.0
- **Database**: SQLite (default) or PostgreSQL (production)
- **Authentication**: Token Authentication
- **CORS**: django-cors-headers
- **Python**: 3.8+

### Apps Structure
```
internship_system/
├── users/          # User authentication and profiles
├── internships/    # Internship listings and applications
├── maintenance/    # Maintenance request management
├── aob/           # Any Other Business requests
└── internship_system/  # Project settings and configuration
```

## Installation & Setup

### 1. Prerequisites
- Python 3.8 or higher
- pip or pipenv (package manager)
- Git
- Virtual environment (recommended)

### 2. Clone the Repository
```bash
git clone <repository-url>
cd internship-system-development/backend
```

### 3. Create Virtual Environment

#### Using venv:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Using pipenv:
```bash
pipenv shell
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

Or if using pipenv:
```bash
pipenv install
```

### 5. Environment Configuration

Create a `.env` file in the backend directory:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
CSRF_TRUSTED_ORIGINS=http://localhost:5173,http://localhost:3000
```

If you are using Supabase Postgres, set `DATABASE_URL` to the Supabase connection string:
```
DATABASE_URL=postgres://postgres:<password>@db.<project>.supabase.co:5432/postgres
```

Note: Change these settings for production!

### 6. Run Migrations
```bash
python manage.py migrate
```

### 7. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 8. Populate Sample Data
```bash
python manage.py populate_db
```

This creates test users and sample data for development:
- **Admin**: admin@example.com / admin123
- **Student**: student1@university.edu / student123
- **Company**: company1@techcorp.com / company123

### 9. Run Development Server
```bash
python manage.py runserver
```

The API will be available at:
- API: http://127.0.0.1:8000/api/
- Admin Panel: http://127.0.0.1:8000/admin/
- API Documentation: Check [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

## Project Structure

```
backend/
├── aob/                    # Any Other Business app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── internships/            # Internships app
│   ├── management/
│   │   └── commands/
│   │       └── populate_db.py  # Data population command
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── maintenance/            # Maintenance requests app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── users/                  # User authentication app
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── internship_system/      # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── permissions.py      # Custom permissions
├── manage.py
├── db.sqlite3
├── requirements.txt
├── API_DOCUMENTATION.md
└── README.md
```

## Key Features

### 1. User Management
- Custom user model with roles (Student, Admin, Company)
- Token-based authentication
- User registration and login
- User profile management

### 2. Internship Management
- Create and list internships
- Search and filter internships by status
- Apply for internships
- Track application status
- Pagination support

### 3. Maintenance Requests
- Submit maintenance requests
- Track request status (pending, in_progress, completed, cancelled)
- Assign and update requests
- Paginated listing with search

### 4. AOB (Any Other Business)
- Submit general inquiries or concerns
- Categorize requests (payment, allocation, support, other)
- Admin review and response system
- Status tracking (pending, in_review, approved, rejected, resolved)

### 5. Admin Dashboard
- User management
- Internship approval workflow
- Maintenance request tracking
- AOB request handling

## API Endpoints Summary

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `GET /api/auth/me/` - Get current user info

### Internships
- `GET /api/internships/` - List internships
- `POST /api/internships/` - Create internship (Admin)
- `GET /api/internships/{id}/` - Get internship details
- `POST /api/internships/{id}/apply/` - Apply for internship

### Applications
- `GET /api/applications/` - List my applications
- `GET /api/applications/{id}/` - Get application details

### Maintenance
- `GET /api/maintenance/` - List maintenance requests
- `POST /api/maintenance/` - Create maintenance request
- `GET /api/maintenance/{id}/` - Get request details
- `PATCH /api/maintenance/{id}/` - Update request status

### AOB Requests
- `GET /api/aob/` - List AOB requests
- `POST /api/aob/` - Create AOB request
- `GET /api/aob/{id}/` - Get request details
- `POST /api/aob/{id}/approve/` - Approve request (Admin)
- `POST /api/aob/{id}/reject/` - Reject request (Admin)
- `POST /api/aob/{id}/resolve/` - Resolve request (Admin)

See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for detailed endpoint documentation.

## Database Models

### CustomUser
```python
- email (EmailField, unique)
- name (CharField)
- username (CharField)
- user_type (CharField: student, admin, company)
- phone (CharField)
- bio (TextField)
- company_name (CharField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### Internship
```python
- title (CharField)
- description (TextField)
- company (CharField)
- duration (CharField)
- status (CharField: active, closed, pending)
- created_by (ForeignKey to CustomUser)
- created_at (DateTimeField)
- updated_at (DateTimeField)
```

### InternshipApplication
```python
- internship (ForeignKey)
- applicant (ForeignKey to CustomUser)
- status (CharField: pending, approved, rejected)
- applied_at (DateTimeField)
```

### MaintenanceRequest
```python
- room (CharField)
- issue (TextField)
- status (CharField: pending, in_progress, completed, cancelled)
- requested_by (ForeignKey to CustomUser)
- created_at (DateTimeField)
- updated_at (DateTimeField)
- resolved_at (DateTimeField)
```

### AOBRequest
```python
- title (CharField)
- description (TextField)
- category (CharField: payment, allocation, support, other)
- status (CharField: pending, in_review, approved, rejected, resolved)
- submitted_by (ForeignKey to CustomUser)
- reviewed_by (ForeignKey to CustomUser)
- response (TextField)
- created_at (DateTimeField)
- updated_at (DateTimeField)
- resolved_at (DateTimeField)
```

## Management Commands

### Populate Database with Sample Data
```bash
python manage.py populate_db
```

Creates sample users, internships, maintenance requests, and AOB requests for testing.

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser
```bash
python manage.py createsuperuser
```

### Run Development Server
```bash
python manage.py runserver [port]
```

### Run Tests
```bash
python manage.py test
```

## Configuration

### Settings File (internship_system/settings.py)

Key configurations:
- `DEBUG`: Set to False in production
- `SECRET_KEY`: Keep secure, use environment variables
- `ALLOWED_HOSTS`: Add production domain
- `DATABASES`: Configure PostgreSQL for production
- `CORS_ALLOWED_ORIGINS`: Add frontend URL
- `REST_FRAMEWORK`: Authentication and permission settings

### CORS Configuration

Update `CORS_ALLOWED_ORIGINS` in settings.py:
```python
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',    # React Vite dev server
    'http://localhost:3000',    # Alternative frontend
    'https://yourdomain.com',   # Production domain
]
```

## Security Considerations

### Development
- DEBUG = True (for error details)
- SQLite database (sufficient for dev)
- Allow all hosts for testing

### Production Checklist
- [ ] Set DEBUG = False
- [ ] Update SECRET_KEY with a secure random value
- [ ] Use PostgreSQL database
- [ ] Set appropriate ALLOWED_HOSTS
- [ ] Configure HTTPS/SSL
- [ ] Set secure CORS origins
- [ ] Use environment variables for secrets
- [ ] Enable CSRF protection
- [ ] Implement rate limiting
- [ ] Set up proper logging
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Configure reverse proxy (Nginx)

## Deployment

### Using Gunicorn and Nginx

#### 1. Install Gunicorn
```bash
pip install gunicorn
```

#### 2. Run with Gunicorn
```bash
gunicorn internship_system.wsgi:application --bind 0.0.0.0:8000
```

#### 3. Nginx Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /path/to/backend/static/;
    }
}
```

### Using Docker

Create Dockerfile:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "internship_system.wsgi:application", "--bind", "0.0.0.0:8000"]
```

Build and run:
```bash
docker build -t internship-system-backend .
docker run -p 8000:8000 internship-system-backend
```

## Troubleshooting

### 1. Migrations Issues
```bash
# Clear migrations (only in development)
python manage.py migrate internships zero
python manage.py migrate users zero
python manage.py migrate aob zero
python manage.py migrate maintenance zero

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

### 2. Static Files
```bash
python manage.py collectstatic
```

### 3. Database Errors
```bash
# Reset database (development only)
rm db.sqlite3
python manage.py migrate
python manage.py populate_db
```

### 4. ModuleNotFoundError
Ensure virtual environment is activated and all requirements installed:
```bash
pip install -r requirements.txt
```

## Testing

### Run All Tests
```bash
python manage.py test
```

### Run Specific App Tests
```bash
python manage.py test users
python manage.py test internships
python manage.py test maintenance
python manage.py test aob
```

### Run Specific Test
```bash
python manage.py test users.tests.UserTestCase.test_registration
```

## Performance Optimization

1. **Database Indexing**: Add indexes on frequently queried fields
2. **Caching**: Implement Redis caching for frequent queries
3. **Pagination**: Always paginate large result sets
4. **Filtering**: Use database-level filtering instead of Python
5. **Monitoring**: Use Django Debug Toolbar in development

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [API Documentation](./API_DOCUMENTATION.md)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Support and Maintenance

For issues or questions:
1. Check the API Documentation
2. Review Django/DRF official documentation
3. Check project issues/discussions
4. Contact the development team

---

**Last Updated**: June 4, 2026
**Version**: 1.0
