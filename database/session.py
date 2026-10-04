from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# استخدام قاعدة بيانات SQLite المحلية المدمجة في بايثون تلقائياً بدون حزم خارجية
DATABASE_URL = "sqlite:///./enterprise_db.db"

# إنشاء المحرك مع إعدادات خاصة بـ SQLite لضمان توافقية المسارات
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)

# تجهيز صانع الجلسات القياسي
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
