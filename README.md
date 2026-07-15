# Task Manager API

A production-style FastAPI backend project for learning and practicing modern backend development concepts. The project includes authentication, task management, PostgreSQL integration, Alembic migrations, JWT-based auth, password hashing, and API testing.

## Overview

This repository is designed as a hands-on learning project for understanding:

- REST API design with FastAPI
- SQLAlchemy ORM and PostgreSQL
- Authentication and authorization
- Password hashing with bcrypt
- JWT token generation and validation
- Database migrations with Alembic
- Testing with pytest
- Containerization with Docker

## Features

### Authentication
- User registration
- User login
- JWT access token generation
- Password hashing with bcrypt
- Protected routes for authenticated users

### Task Management
- Create tasks
- List tasks for the authenticated user
- Get a specific task
- Update a task
- Delete a task

## Tech Stack

- Python 3.13+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT via python-jose
- bcrypt/passlib
- pytest
- Docker

## Project Structure

```text
app/
  api/routes/       # API route handlers
  core/             # config, security, exceptions, logging
  database/         # DB session and dependency wiring
  models/           # SQLAlchemy models
  repositories/     # DB access layer
  schemas/          # request/response schemas
  services/         # business logic
  utils/            # shared helpers
alembic/            # migration files and config
tests/              # pytest test suite
docs/               # project notes and learning guide
requirements.txt   # Python dependencies
Dockerfile          # container definition
```

## Prerequisites

Before running the project, make sure you have:

- Python 3.13+
- PostgreSQL running locally or via Docker
- pip installed
- Optional: Docker for containerized setup

## Environment Variables

Create a `.env` file in the project root with values like:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/task_manager_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=true
```

## Local Development Setup

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start PostgreSQL

If you are using Docker, run PostgreSQL with a container:

```bash
docker run --name task-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=task_manager_db -p 5432:5432 -d postgres:16
```

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start the application

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- http://127.0.0.1:8000/docs for Swagger UI
- http://127.0.0.1:8000/redoc for ReDoc

## API Endpoints

### Authentication
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

### Tasks
- POST `/tasks/`
- GET `/tasks/`
- GET `/tasks/{task_id}`
- PUT `/tasks/{task_id}`
- DELETE `/tasks/{task_id}`

## Running Tests

```bash
pytest
```

Or for a specific test file:

```bash
pytest tests/test_auth_api.py
```

## Docker

Build the image:

```bash
docker build -t task-manager-api .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env task-manager-api
```

## Security Notes

- Never commit `.env` files or secrets
- Use strong `SECRET_KEY` values in production
- Keep database credentials private
- Rotate secrets if they are exposed

## Notes for Learning

This project is intentionally structured to help you understand backend architecture step by step, including:

- separation of concerns
- service and repository layers
- dependency injection
- environment-based configuration
- API authentication
- database migrations
