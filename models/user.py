import uuid
from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base

class User(Base):
    __tablename__ = "users"

    # استخدام معرفات UUID الفريدة لأمان قواعد البيانات
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
    # تحديد مستوى صلاحيات الموظفين: Admin, Manager, Developer
    role: Mapped[str] = mapped_column(String(20), default="Developer", nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
