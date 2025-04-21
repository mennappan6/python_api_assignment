
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, default="running")
    created_at = Column(DateTime, default=datetime.utcnow)
