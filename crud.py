
from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(name=task.name)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task_status(db: Session, task_id: int, status: str):
    task = get_task_by_id(db, task_id)
    if task:
        task.status = status
        db.commit()
        db.refresh(task)
    return task