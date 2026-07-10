from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

app = FastAPI(
    title="Task Manager API",
    description="Production-ready Task Management API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Task Manager API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-check")
def check_database():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "Connected Successfully"
        }

    except Exception as e:
        return {
            "database": "Connection Failed",
            "error": str(e)
        }