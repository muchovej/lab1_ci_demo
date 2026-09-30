# Lab 1 Reference Solution

A minimal FastAPI service with `/hello`, `/health`, `/docs`, and `/openapi.json` endpoints, packaged as a multi-stage Docker image.

## What this app does

- `GET /hello?name=<value>` returns `{"message": "Hello <value>"}`. Missing `name` returns HTTP 422.
- `GET /health` returns `{"status": "healthy"}`.
- `GET /` returns FastAPI's default 404.
- `GET /docs` serves the Swagger UI.
- `GET /openapi.json` serves the OpenAPI 3.1 schema.

## Build

```bash
poetry install
docker build -t lab1 .
```

## Run

Local (auto-reload during development):

```bash
poetry run uvicorn src.main:app --reload
```

Container:

```bash
docker run --rm -p 8000:8000 lab1
```

Visit <http://localhost:8000/docs>.

## Test

```bash
poetry run pytest
poetry run ruff check .
poetry run ruff format --check .
```
# lab1_ci_demo
