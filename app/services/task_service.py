from sqlalchemy.orm import Session

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

        return task_repository.create_task(
            db,
            task,
        )

    def get_tasks(
        self,
        db: Session,
        current_user: User,
    ):

        return task_repository.get_tasks_by_owner(
            db,
            current_user.id,
        )

    def get_task(
        self,
        db: Session,
        task_id: int,
        current_user: User,
    ):

        task = task_repository.get_task_by_id(
            db,
            task_id,
        )

        if task is None:
            raise ValueError("Task not found")

        if task.owner_id != current_user.id:
            raise ValueError("Access denied")

        return task

    def update_task(
        self,
        db: Session,
        task_id: int,
        task_data: TaskUpdate,
        current_user: User,
    ):

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

        return task_repository.update_task(
            db,
            task,
        )

    def delete_task(
        self,
        db: Session,
        task_id: int,
        current_user: User,
    ):

        task = self.get_task(
            db,
            task_id,
            current_user,
        )

        task_repository.delete_task(
            db,
            task,
        )


task_service = TaskService()