from fastapi import FastAPI
from sqlalchemy import text
from app.api.routes.auth import router as auth_router
from app.database.database import engine
from app.api.routes.task import router as task_router

from app.core.exception_handlers import register_exception_handlers


app = FastAPI(
    title="Task Manager API",
    description="Production-ready Task Management API",
    version="1.0.0"
)
app.include_router(auth_router)
app.include_router(task_router)
register_exception_handlers(app)

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