# Internship System API Documentation

## Backend Architecture

This is a Django REST Framework backend for the University Internship System. The API follows RESTful conventions and provides endpoints for user authentication, internship management, maintenance requests, and general inquiries (AOB).

### Base URL
```
http://localhost:8000/api/
```

### Authentication
The API uses Token Authentication. Include the token in the Authorization header:
```
Authorization: Token <your_token_here>
```

---

## Endpoints

### 1. Authentication Endpoints

#### Register a New User
- **URL:** `/api/auth/register/`
- **Method:** `POST`
- **Authentication:** Not required
- **Request Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword123",
  "password_confirm": "securepassword123",
  "user_type": "student",
  "phone": "1234567890",
  "company_name": null
}
```
- **Response (201 Created):**
```json
{
  "token": "abc123def456...",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "username": "user@example.com",
    "user_type": "student",
    "phone": "1234567890",
    "bio": null,
    "company_name": null,
    "created_at": "2026-06-04T10:00:00Z"
  }
}
```

#### Login
- **URL:** `/api/auth/login/`
- **Method:** `POST`
- **Authentication:** Not required
- **Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```
- **Response (200 OK):**
```json
{
  "token": "abc123def456...",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "username": "user@example.com",
    "user_type": "student",
    "phone": "1234567890",
    "bio": null,
    "company_name": null,
    "created_at": "2026-06-04T10:00:00Z"
  }
}
```

#### Get Current User Info
- **URL:** `/api/auth/me/`
- **Method:** `GET`
- **Authentication:** Required
- **Response (200 OK):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",
  "username": "user@example.com",
  "user_type": "student",
  "phone": "1234567890",
  "bio": null,
  "company_name": null,
  "created_at": "2026-06-04T10:00:00Z"
}
```

#### Logout
- **URL:** `/api/auth/logout/`
- **Method:** `POST`
- **Authentication:** Required
- **Response (200 OK):**
```json
{
  "detail": "Logged out successfully."
}
```

---

### 2. Internship Management Endpoints

#### List All Internships
- **URL:** `/api/internships/`
- **Method:** `GET`
- **Authentication:** Not required (but read-only)
- **Query Parameters:**
  - `page`: Page number (default: 1)
  - `page_size`: Items per page (default: 10, max: 100)
  - `search`: Search by title, company, or description
  - `status`: Filter by status (active, closed, pending)
  - `ordering`: Order by field (e.g., -created_at, status)
- **Response (200 OK):**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/internships/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Summer Internship 2026",
      "description": "Web development internship",
      "company": "Tech Corp",
      "duration": "3 months",
      "status": "active",
      "created_by": {
        "id": 2,
        "email": "admin@example.com",
        "name": "Admin User",
        "username": "admin@example.com",
        "user_type": "admin",
        "phone": null,
        "bio": null,
        "company_name": null,
        "created_at": "2026-06-04T09:00:00Z"
      },
      "created_at": "2026-06-04T10:00:00Z",
      "updated_at": "2026-06-04T10:00:00Z"
    }
  ]
}
```

#### Create New Internship (Admin only)
- **URL:** `/api/internships/`
- **Method:** `POST`
- **Authentication:** Required (Admin)
- **Request Body:**
```json
{
  "title": "Summer Internship 2026",
  "description": "Web development internship",
  "company": "Tech Corp",
  "duration": "3 months",
  "status": "active"
}
```
- **Response (201 Created):** Same as list item above

#### Get Internship Details
- **URL:** `/api/internships/{id}/`
- **Method:** `GET`
- **Authentication:** Not required
- **Response (200 OK):** Same as list item above

#### Update Internship (Admin only)
- **URL:** `/api/internships/{id}/`
- **Method:** `PUT` or `PATCH`
- **Authentication:** Required (Admin)
- **Request Body:** Same as create
- **Response (200 OK):** Updated internship object

#### Delete Internship (Admin only)
- **URL:** `/api/internships/{id}/`
- **Method:** `DELETE`
- **Authentication:** Required (Admin)
- **Response (204 No Content)**

#### Apply for Internship
- **URL:** `/api/internships/{id}/apply/`
- **Method:** `POST`
- **Authentication:** Required
- **Response (201 Created):**
```json
{
  "detail": "Application submitted."
}
```

---

### 3. Internship Applications Endpoints

#### List My Applications
- **URL:** `/api/applications/`
- **Method:** `GET`
- **Authentication:** Required
- **Query Parameters:**
  - `page`: Page number (default: 1)
  - `search`: Search by internship title or company
  - `ordering`: Order by field (e.g., -applied_at)
- **Response (200 OK):**
```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "internship": {
        "id": 1,
        "title": "Summer Internship 2026",
        "description": "Web development internship",
        "company": "Tech Corp",
        "duration": "3 months",
        "status": "active",
        "created_by": {...},
        "created_at": "2026-06-04T10:00:00Z",
        "updated_at": "2026-06-04T10:00:00Z"
      },
      "applicant": {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe",
        "username": "user@example.com",
        "user_type": "student",
        "phone": "1234567890",
        "bio": null,
        "company_name": null,
        "created_at": "2026-06-04T10:00:00Z"
      },
      "status": "pending",
      "applied_at": "2026-06-04T11:30:00Z"
    }
  ]
}
```

#### Get Application Details
- **URL:** `/api/applications/{id}/`
- **Method:** `GET`
- **Authentication:** Required
- **Response (200 OK):** Same as above

---

### 4. Maintenance Request Endpoints

#### List Maintenance Requests
- **URL:** `/api/maintenance/`
- **Method:** `GET`
- **Authentication:** Required
- **Query Parameters:**
  - `page`: Page number
  - `page_size`: Items per page
  - `search`: Search by room or issue
  - `status`: Filter by status (pending, in_progress, completed, cancelled)
  - `ordering`: Order by field
- **Response (200 OK):**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "room": "Room 101",
      "issue": "Broken window",
      "status": "pending",
      "requested_by": {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe",
        "username": "user@example.com",
        "user_type": "student",
        "phone": "1234567890",
        "bio": null,
        "company_name": null,
        "created_at": "2026-06-04T10:00:00Z"
      },
      "created_at": "2026-06-04T10:00:00Z",
      "updated_at": "2026-06-04T10:00:00Z",
      "resolved_at": null
    }
  ]
}
```

#### Create Maintenance Request
- **URL:** `/api/maintenance/`
- **Method:** `POST`
- **Authentication:** Required
- **Request Body:**
```json
{
  "room": "Room 101",
  "issue": "Broken window"
}
```
- **Response (201 Created):** Same as list item above

#### Get Maintenance Request Details
- **URL:** `/api/maintenance/{id}/`
- **Method:** `GET`
- **Authentication:** Required
- **Response (200 OK):** Same as list item above

#### Update Maintenance Request
- **URL:** `/api/maintenance/{id}/`
- **Method:** `PUT` or `PATCH`
- **Authentication:** Required (Owner or Admin)
- **Request Body:**
```json
{
  "room": "Room 101",
  "issue": "Broken window",
  "status": "in_progress"
}
```
- **Response (200 OK):** Updated request object

#### Delete Maintenance Request
- **URL:** `/api/maintenance/{id}/`
- **Method:** `DELETE`
- **Authentication:** Required (Owner or Admin)
- **Response (204 No Content)**

---

### 5. AOB (Any Other Business) Request Endpoints

#### List AOB Requests
- **URL:** `/api/aob/`
- **Method:** `GET`
- **Authentication:** Required
- **Query Parameters:**
  - `page`: Page number
  - `page_size`: Items per page
  - `search`: Search by title or description
  - `status`: Filter by status (pending, in_review, approved, rejected, resolved)
  - `ordering`: Order by field
- **Response (200 OK):**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Payment inquiry",
      "description": "Question about internship stipend payment",
      "category": "payment",
      "status": "pending",
      "submitted_by": {
        "id": 1,
        "email": "user@example.com",
        "name": "John Doe",
        "username": "user@example.com",
        "user_type": "student",
        "phone": "1234567890",
        "bio": null,
        "company_name": null,
        "created_at": "2026-06-04T10:00:00Z"
      },
      "reviewed_by": null,
      "response": null,
      "created_at": "2026-06-04T10:00:00Z",
      "updated_at": "2026-06-04T10:00:00Z",
      "resolved_at": null
    }
  ]
}
```

#### Create AOB Request
- **URL:** `/api/aob/`
- **Method:** `POST`
- **Authentication:** Required
- **Request Body:**
```json
{
  "title": "Payment inquiry",
  "description": "Question about internship stipend payment",
  "category": "payment"
}
```
- **Response (201 Created):** Same as list item above

#### Get AOB Request Details
- **URL:** `/api/aob/{id}/`
- **Method:** `GET`
- **Authentication:** Required
- **Response (200 OK):** Same as list item above

#### Approve AOB Request (Admin only)
- **URL:** `/api/aob/{id}/approve/`
- **Method:** `POST`
- **Authentication:** Required (Admin)
- **Response (200 OK):**
```json
{
  "detail": "Request approved."
}
```

#### Reject AOB Request (Admin only)
- **URL:** `/api/aob/{id}/reject/`
- **Method:** `POST`
- **Authentication:** Required (Admin)
- **Request Body:**
```json
{
  "response": "This request cannot be approved at this time."
}
```
- **Response (200 OK):**
```json
{
  "detail": "Request rejected."
}
```

#### Resolve AOB Request (Admin only)
- **URL:** `/api/aob/{id}/resolve/`
- **Method:** `POST`
- **Authentication:** Required (Admin)
- **Response (200 OK):**
```json
{
  "detail": "Request resolved."
}
```

---

## User Types

The system supports three user types:
- **student**: Regular student users
- **admin**: Administrator users with full access
- **company**: Company representatives posting internships

---

## Status Codes

- **200 OK**: Successful request
- **201 Created**: Resource created successfully
- **204 No Content**: Successful delete
- **400 Bad Request**: Invalid request data
- **401 Unauthorized**: Authentication required or failed
- **403 Forbidden**: Permission denied
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

---

## Error Response Format

```json
{
  "detail": "Error message description",
  "field_name": ["Field-specific error message"]
}
```

---

## Running the Backend

### Installation

1. Install Python 3.8+
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`
Admin panel: `http://localhost:8000/admin/`

---

## Testing the API

You can test the API endpoints using:
- **Postman**: Import the endpoints and test them manually
- **cURL**: Use curl commands to test endpoints
- **Python**: Use requests library to write test scripts
- **Frontend**: Connect your React frontend to consume these APIs

Example using cURL:
```bash
# Register
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"John","password":"pass123","password_confirm":"pass123","user_type":"student"}'

# Login
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"pass123"}'

# Get internships
curl -X GET http://localhost:8000/api/internships/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## Security Notes

- Always use HTTPS in production
- Keep your secret key secure
- Use environment variables for sensitive settings
- Implement rate limiting for production
- Enable CSRF protection
- Validate all user inputs
- Use strong password policies
