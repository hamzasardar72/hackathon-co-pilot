# Deployment Guide

## Local Development

1. Activate the Python virtual environment.
2. Install backend dependencies:
   `pip install -r backend/requirements.txt`
3. Install frontend dependencies:
   `npm install --prefix frontend`
4. Start the API:
   `uvicorn backend.app.main:app --reload`
5. Start the frontend:
   `npm start --prefix frontend`

## Docker

Run:

```bash
docker compose up --build
```

This launches the FastAPI service and PostgreSQL container.
