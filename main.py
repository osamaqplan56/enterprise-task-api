from fastapi import FastAPI
# قمنا بتحديد المسار الكامل والصحيح للاستيراد طبقاً لهيكلك الاحترافي الحالي
from app.routers import auth, projects, tasks

app = FastAPI(
    title="Enterprise Task Management API",
    description="نظام متقدم لإدارة مهام ومشاريع الفرق البرمجية عن بعد - معرض أعمال أسامة",
    version="1.0.0"
)

# ربط المسارات بالخادم الرئيسي
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {
        "status": "success",
        "message": "Welcome to Enterprise Task Management API! Everything is running smoothly.",
        "developer": "Osama"
    }
