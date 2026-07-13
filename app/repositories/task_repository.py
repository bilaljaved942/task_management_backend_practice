from sqlalchemy.orm import Session

from app.models.task import Task


class TaskRepository:

    def create_task(
        self,
        db: Session,
        task: Task,
    ) -> Task:

        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    def get_tasks_by_owner(
        self,
        db: Session,
        owner_id: int,
    ) -> list[Task]:

        return (
            db.query(Task)
            .filter(Task.owner_id == owner_id)
            .order_by(Task.created_at.desc())
            .all()
        )

    def get_task_by_id(
        self,
        db: Session,
        task_id: int,
    ) -> Task | None:

        return (
            db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )

    def update_task(
        self,
        db: Session,
        task: Task,
    ) -> Task:

        db.commit()
        db.refresh(task)

        return task

    def delete_task(
        self,
        db: Session,
        task: Task,
    ):

        db.delete(task)
        db.commit()


task_repository = TaskRepository()