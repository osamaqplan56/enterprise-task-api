from fastapi import APIRouter
from pydantic import BaseModel
import uuid

# تأكيد تسمية المتغير بـ router بدقة ليتعرف عليه ملف main.py
router = APIRouter(prefix="/projects", tags=["Projects"])

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

@router.post("/create")
async def create_project(project_data: ProjectCreate):
    return {
        "status": "success",
        "message": f"Project '{project_data.name}' has been created successfully!",
        "project_id": str(uuid.uuid4()),
        "details": {
            "name": project_data.name,
            "description": project_data.description
        }
    }
