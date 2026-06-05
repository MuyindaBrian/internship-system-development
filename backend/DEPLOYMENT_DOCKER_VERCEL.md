# Docker + Vercel Deployment for Django Backend

This guide covers deploying the Django backend in `backend/` using Docker locally and using Vercel with a Docker container.

## Dockerfile

The repository includes a `backend/Dockerfile` that:
- uses Python 3.11
- installs dependencies from `requirements.txt`
- collects static files with `collectstatic`
- starts the app with Gunicorn

## Local Docker development

From the `backend/` directory:

```bash
docker build -t internship-backend .
docker run -p 8000:8000 \
  -e DEBUG=False \
  -e SECRET_KEY='your-secret-key' \
  -e DATABASE_URL='postgres://postgres:password@host:5432/postgres' \
  -e CORS_ALLOWED_ORIGINS='http://localhost:5173,http://localhost:3000' \
  -e CSRF_TRUSTED_ORIGINS='http://localhost:5173,http://localhost:3000' \
  internship-backend
```

### Local development with docker-compose

The `backend/docker-compose.yml` file provides a local Postgres service and Django web service.

Run:

```bash
docker compose up --build
```

Then visit:

- `http://localhost:8000/api/`
- `http://localhost:8000/admin/`

## Vercel Docker deployment

This backend is ready for Vercel deployment using a Docker container.

### Important files

- `backend/vercel.json`
- `backend/Dockerfile`
- `backend/.dockerignore`

### Vercel setup

1. In Vercel, create or select a project.
2. Set the project root to `backend/`.
3. Add environment variables in Vercel:

```text
SECRET_KEY=your-production-secret
DEBUG=False
ALLOWED_HOSTS=<your-vercel-host>
DATABASE_URL=postgres://postgres:<password>@db.<project>.supabase.co:5432/postgres
CORS_ALLOWED_ORIGINS=https://<your-frontend-domain>
CSRF_TRUSTED_ORIGINS=https://<your-frontend-domain>
```

4. Deploy the project.

### Notes

- `vercel.json` uses `@vercel/docker` to build the Django container.
- For a Supabase database, the backend `DATABASE_URL` should include Postgres credentials and host.
- The container listens on port `8000`.

## Troubleshooting

- If static files are missing, confirm `collectstatic` completed and the container has `STATIC_ROOT` configured.
- If the database cannot connect, verify the `DATABASE_URL` and that SSL requirements are met.
- If Vercel build fails, check that `Dockerfile` is in the `backend/` directory and your project root is set correctly.
