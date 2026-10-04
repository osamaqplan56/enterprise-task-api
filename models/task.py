import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    
    # حالات المهمة المتوقعة للفرق البرمجية (Todo, In_Progress, Review, Done)
    status: Mapped[str] = mapped_column(String(20), default="Todo", nullable=False)
    
    # مستوى الأهمية (Low, Medium, High)
    priority: Mapped[str] = mapped_column(String(20), default="Medium", nullable=False)
    
    # ربط المهمة بالمشروع التابع له (حذف المهام تلقائياً عند حذف المشروع)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    
    # ربط المهمة بالمطور المسؤول عن تنفيذها (اختياري)
    assigned_to: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    due_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
