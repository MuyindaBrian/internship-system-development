# Deploying to Railway (using Supabase Postgres)

1. Ensure your repository is connected to Railway (you mentioned it is).
2. Add these environment variables in Railway project settings:

```
SECRET_KEY=your-production-secret
DEBUG=False
ALLOWED_HOSTS=<your-railway-app-host>
CORS_ALLOWED_ORIGINS=https://<your-frontend-domain>
CSRF_TRUSTED_ORIGINS=https://<your-frontend-domain>
DATABASE_URL=postgres://postgres:<password>@db.<project>.supabase.co:5432/postgres
```

3. Set Railway build and start commands (if Railway doesn't auto-detect):

Build command:

```
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
```

Start command (Procfile is recommended):

```
web: gunicorn internship_system.wsgi --bind 0.0.0.0:$PORT
```

4. After deploy, verify migrations ran and that static files are served. If static files 404, ensure `STATIC_ROOT` is set and the `collectstatic` step ran.

Notes:
- Railway will build the app using `runtime.txt` to select Python 3.11.
- We added WhiteNoise so static files are served by Django + Gunicorn.
- Supabase provides Postgres; we enable `sslmode=require` for hosts under `supabase.co`.
