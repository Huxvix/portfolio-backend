# Portfolio Backend

This repository is the headless backend that powers my portfolio website. It exposes a clean REST API for personal information, skills, projects, and contact messages so the frontend can stay lightweight while content lives in one maintainable place.

## Why it matters
- **Purpose-built content service**: Django REST Framework keeps responses predictable for the portfolio frontend and any future clients (mobile, CLI, etc.).
- **Production ready**: Environment-driven settings, CORS fencing, and Gunicorn/Procfile deployment make it easy to host on Render, Railway, or any container platform.
- **Media friendly**: Cloudinary handles profile pictures, project shots, and résumé files, so assets stay cached and fast worldwide.
- **Simple authoring**: Update records through Django Admin or migrations without touching frontend code.

## Tech stack
- Django 5.2, Django REST Framework 3.16
- PostgreSQL (via `dj-database-url`) in production, SQLite fallback locally
- Cloudinary + `django-cloudinary-storage` for media
- Whitenoise for static files, `django-cors-headers` for controlled cross-origin access
- Gunicorn process model for deployment

## API surface
| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/personal-info/` | GET | Returns the headline profile block (name, title, bio, contact links, résumé URL, availability message).
| `/api/skills/` | GET | Lists active skills grouped by category with icon metadata.
| `/api/projects/` | GET | Returns portfolio projects, their hero image, outbound links, and related skills.
| `/api/contact/` | POST | Validates and stores lead messages so I can follow up from the admin.

## Project layout
```
backend/           # Django project settings and root URLs
core/              # Personal info + skills models, serializers, views
projects/          # Project showcase domain
contact/           # Contact form endpoint and storage
staticfiles/       # Collected static assets for admin/UI
manage.py          # Django management entry point
Procfile           # Gunicorn command used in production
requirements.txt   # Locked dependencies
```

## Local development
1. **Clone and install**
   ```bash
   git clone https://github.com/Huxvix/portfolio-backend.git
   cd portfolio-backend
   python -m venv .venv
   .venv\Scripts\activate  # Mac/Linux: source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Configure environment** — copy `.env.example` (create one if needed) and set the variables listed below.
3. **Apply migrations and seed data**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser  # optional but handy for admin access
   ```
4. **Run the server**
   ```bash
   python manage.py runserver
   ```
   The browsable API lives at `http://127.0.0.1:8000/`.

## Environment variables
| Variable | Description |
| --- | --- |
| `SECRET_KEY` | Django secret key; generate a new value for each environment.
| `DEBUG` | `True` locally, `False` in production.
| `ALLOWED_HOSTS` | Comma-separated list of hostnames serving the app.
| `DATABASE_URL` | PostgreSQL/Neon connection string (falls back to SQLite when omitted).
| `CORS_ALLOWED_ORIGINS` | Comma-separated list of frontend origins allowed to call the API.
| `CLOUDINARY_URL` | Standard Cloudinary connection URL for media storage.

## Testing
```bash
python manage.py test
```
This command runs the test suites in `core`, `projects`, and `contact`. Add coverage as you expand the API surface.

## Deployment checklist
- Collect static files if the host requires it: `python manage.py collectstatic`.
- Ensure `DEBUG=False`, `ALLOWED_HOSTS`, and `CORS_ALLOWED_ORIGINS` are set.
- Provide `DATABASE_URL` with SSL enabled (Neon style) so Django connects securely.
- Use the included `Procfile` (`web: gunicorn backend.wsgi`) for platforms that auto-detect process definitions.

## Roadmap ideas
- Token-protected endpoints for managing content programmatically.
- Pagination and caching for the project list as the portfolio grows.
- Webhook or email notifications whenever a new contact message lands.
