from sqlalchemy.orm import Session

from app.core.exceptions import (
    PermissionDeniedError,
    TaskNotFoundError,
)
from app.core.logging import logger
from app.models.task import Task
from app.models.user import User
from app.repositories.task_repository import task_repository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:

    def create_task(
        self,
        db: Session,
        task_data: TaskCreate,
        current_user: User,
    ) -> Task:

        task = Task(
            title=task_data.title,
            description=task_data.description,
            owner_id=current_user.id,
        )

        saved_task = task_repository.create_task(
            db,
            task,
        )

        logger.info(
            "Task %s created by user %s",
            saved_task.id,
            current_user.email,
        )

        return saved_task

    def get_tasks(
        self,
        db: Session,
        current_user: User,
    ) -> list[Task]:

        return task_repository.get_tasks_by_owner(
            db,
            current_user.id,
        )

    def get_task(
        self,
        db: Session,
        task_id: int,
        current_user: User,
    ) -> Task:

        task = task_repository.get_task_by_id(
            db,
            task_id,
        )

        if task is None:
            raise TaskNotFoundError()

        if task.owner_id != current_user.id:
            logger.warning(
                "User %s tried to access task %s owned by another user",
                current_user.email,
                task_id,
            )
            raise PermissionDeniedError()

        return task

    def update_task(
        self,
        db: Session,
        task_id: int,
        task_data: TaskUpdate,
        current_user: User,
    ) -> Task:

        task = self.get_task(
            db,
            task_id,
            current_user,
        )

        update_data = task_data.model_dump(
            exclude_unset=True,
        )

        for key, value in update_data.items():
            setattr(task, key, value)

        updated_task = task_repository.update_task(
            db,
            task,
        )

        logger.info(
            "Task %s updated by user %s",
            updated_task.id,
            current_user.email,
        )

        return updated_task

    def delete_task(
        self,
        db: Session,
        task_id: int,
        current_user: User,
    ) -> None:

        task = self.get_task(
            db,
            task_id,
            current_user,
        )

        task_repository.delete_task(
            db,
            task,
        )

        logger.info(
            "Task %s deleted by user %s",
            task.id,
            current_user.email,
        )


task_service = TaskService()