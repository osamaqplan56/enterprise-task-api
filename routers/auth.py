from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.core.security import get_password_hash  # استيراد دالة التشفير

router = APIRouter(prefix="/auth", tags=["Authentication"])

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "Developer"

@router.post("/register")
async def register_user(user_data: UserRegister):
    # تطبيق التشفير الحقيقي هنا 🔐
    hashed_password = get_password_hash(user_data.password)
    
    return {
        "status": "success",
        "message": f"User {user_data.username} registered with high encryption!",
        "data": {
            "username": user_data.username,
            "email": user_data.email,
            "role": user_data.role,
            "password_in_database": hashed_password  # سنعرض الـ Hash المشفر هنا لنرى النتيجة التفاعلية
        }
    }
