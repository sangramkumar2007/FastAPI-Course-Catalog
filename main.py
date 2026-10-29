from fastapi import FastAPI
from database import engine
from models import Base
from controllers.course_controller import router as course_router
from controllers.enrollment_controller import router as enrollment_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "Course Catalog Manegement System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return{
        "message": "Welcome to Course Catalog Management System"
    }
app.include_router(course_router)
app.include_router(enrollment_router)