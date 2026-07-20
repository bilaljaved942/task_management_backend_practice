# Task Manager API

This repository is a hands-on backend learning project built with FastAPI, SQLAlchemy, PostgreSQL, Alembic, JWT, and bcrypt. It is designed to help someone understand how a real backend application is structured, how different layers communicate, and how common production concerns such as authentication, database migration, dependency injection, testing, containerization, and deployment are handled.

The project currently covers:

- User registration and login
- JWT-based authentication
- Password hashing with bcrypt
- Task creation, retrieval, update, and deletion
- SQLAlchemy models and repository-style data access
- Database migrations with Alembic
- API testing with pytest
- Docker and Kubernetes deployment basics

---

## Why this project exists

This is not just a CRUD app. It is a learning project meant to help you understand backend engineering in depth.

It is useful for learning:

- how APIs are structured and versioned
- how authentication works in real systems
- how database models map to application logic
- how services and repositories separate concerns
- how environment-based configuration is handled
- how code is organized for readability and maintainability
- how deployment and infrastructure concepts connect to application code

---

## Core backend concepts covered

### 1. API layer
The API layer contains the routes and request handling logic.

Examples:
- authentication routes under `app/api/routes/auth.py`
- task routes under `app/api/routes/task.py`

This layer is responsible for:
- receiving HTTP requests
- validating input shape
- calling the appropriate service
- returning responses

### 2. Service layer
The service layer contains business logic.

Examples:
- user registration and login flow
- task lifecycle logic

This layer is responsible for:
- applying business rules
- orchestrating actions across repositories and helpers
- keeping route handlers thin

### 3. Repository layer
The repository layer handles database access logic.

This project uses repository-style abstractions to keep database work separate from business logic.

### 4. Model layer
The model layer defines the database entities using SQLAlchemy.

Examples:
- `User` model
- task model

This is where ORM mappings and table structure live.

### 5. Schema layer
Schemas describe the shape of incoming and outgoing data.

This is important for:
- request validation
- response modeling
- API documentation generation

### 6. Authentication and security
The project includes practical auth concepts such as:

- password hashing with bcrypt
- password verification
- JWT token generation
- protected routes using authentication dependencies

### 7. Database migrations
Alembic is used to manage schema changes over time.

This teaches:
- how migrations are created
- how schema updates are applied safely
- how to evolve a production-style application without losing control

### 8. Configuration management
Configuration is loaded from environment variables using Pydantic settings.

This reflects production practices where secrets and settings should stay outside code.

### 9. Testing
The project includes automated tests for:
- auth flows
- security helpers
- service behavior
- task API behavior

This helps you understand how backend systems are validated.

### 10. Containerization and deployment
The project also includes Docker and Kubernetes deployment files to understand how backend applications are packaged and deployed in real environments.

---

## Tech stack

- Python 3.13+
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic / Pydantic Settings
- python-jose
- bcrypt / passlib
- pytest
- Docker
- Kubernetes manifests

---

## Project structure

```text
app/
  api/
    routes/            # route handlers
  core/                # settings, security, exceptions, logging
  database/            # DB config and session dependencies
  models/              # SQLAlchemy ORM models
  repositories/        # database access helpers
  schemas/             # Pydantic schemas
  services/            # business logic
  utils/               # helper utilities
alembic/               # migration setup and scripts
tests/                 # test cases
docs/                  # project notes and guide
requirements.txt      # Python dependencies
Dockerfile             # container definition
docker-compose.yml    # container orchestration for local services
deployment.yaml        # Kubernetes deployment manifest
```

---

## Features implemented

### Authentication
- User registration endpoint
- Login endpoint
- Token-based authentication
- Protected user profile endpoint
- Password hashing and verification

### Task management
- Create a task
- Retrieve all tasks for current user
- Retrieve a single task
- Update a task
- Delete a task

### Infrastructure basics
- Docker support
- Kubernetes deployment manifest
- Config-based secrets and environment usage

---

## Environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/task_manager_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=true
```

---

## Local setup

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

You can use Docker:

```bash
docker run --name task-postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=task_manager_db -p 5432:5432 -d postgres:16
```

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Swagger UI will be available at:

- http://127.0.0.1:8000/docs

---

## API endpoints

### Authentication
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`

### Tasks
- `POST /tasks/`
- `GET /tasks/`
- `GET /tasks/{task_id}`
- `PUT /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

---

## Testing

Run all tests:

```bash
pytest
```

Run a specific test suite:

```bash
pytest tests/test_auth_api.py
```

---

## Docker

Build the image:

```bash
docker build -t task-manager-api .
```

Run the container:

```bash
docker run -p 8000:8000 --env-file .env task-manager-api
```

---

## Kubernetes notes

The repository includes a deployment manifest for understanding how an application is deployed to Kubernetes.

This is useful for learning:

- pods and deployments
- container ports
- health probes
- resource requests and limits
- config maps and secrets

---

## Security notes

- Never commit `.env` files or secrets
- Keep credentials outside source code
- Use strong secret keys in production
- Use environment-based configuration for sensitive values

---

## Learning roadmap / interview preparation guide

This project can help you prepare for backend-related discussions and interviews.

### Common concepts to understand deeply

- REST API design
- Authentication flow
- JWT vs session-based auth
- Password hashing and salting
- SQLAlchemy ORM basics
- Database migrations
- Dependency injection in FastAPI
- Validation with Pydantic
- Layered architecture
- Testing strategies
- Docker and container basics
- Kubernetes deployment basics

### Good interview talking points

- Why route handlers should stay thin
- Why service layers are useful
- Why repositories help organize persistence logic
- Why hashing passwords is necessary
- Why environment variables matter in production
- Why tests are important for backend reliability
- Why containerization improves portability

---

## Summary

This project is a strong foundation for learning backend development in a practical, structured way. It combines API design, authentication, database work, architecture, testing, and deployment into one cohesive example that can be used both for hands-on practice and for explaining backend concepts to others.
