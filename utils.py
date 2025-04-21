
import time
import threading
from sqlalchemy.orm import Session
from .crud import update_task_status

def simulate_task_lifecycle(db: Session, task_id: int):
    def task_thread():
        time.sleep(5)
        update_task_status(db, task_id, "completed")
    threading.Thread(target=task_thread).start()
