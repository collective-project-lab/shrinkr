# 🔗 Shrinkr
A simple URL shortener built with Django + DRF.

## Tech Stack
- Python 3.11 + uv
- Django + Django REST Framework
- SQLite
- Docker

## Local Setup

### Without Docker
```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

### With Docker
```bash
docker compose up --build
```

Server runs at `http://localhost:8000`

## Environment Variables
Copy `.env.example` to `.env` and fill in:
```
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/shorten/` | Shorten a URL |
| `GET` | `/api/urls/` | List all URLs |
| `GET` | `/{short_code}/` | Redirect to original URL |
| `DELETE` | `/api/urls/{short_code}/` | Delete a URL |

## Running Tests
```bash
uv run python manage.py test
```