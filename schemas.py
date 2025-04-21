
from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    name: str

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
