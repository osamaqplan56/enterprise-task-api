from fastapi import APIRouter
from pydantic import BaseModel
import uuid
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# هيكل البيانات المطلوبة لإنشاء مهمة برمجية جديدة داخل المشروع
class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str = "Medium"       # الأولويات: Low, Medium, High
    project_id: str                # معرف المشروع التابعة له المهمة

@router.post("/create")
async def create_task(task_data: TaskCreate):
    return {
        "status": "success",
        "message": f"Task '{task_data.title}' has been successfully assigned to the project!",
        "task_id": str(uuid.uuid4()),
        "details": {
            "title": task_data.title,
            "priority": task_data.priority,
            "project_id": task_data.project_id,
            "status": "Todo",       # الحالة الافتراضية لأي مهمة جديدة
            "created_at": str(datetime.utcnow())
        }
    }
