from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Course
from schemas import CourseCreate, CourseResponse

router = APIRouter(
    prefix = "/courses",
    tags = ["Courses"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/", response_model = CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(
        title =course.title,
        description = course.description,
        instructor = course.instructor,
        credits = course.credits,
        capacity = course.capacity,
        enrolled_count = course.enrolled_count,
        price= course.price,
        status = course.status
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course  

@router.get("/",response_model= list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses
@router.get("/{course_id}",
            response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code = 404, detail= "Course not found")
    return course
@router.put("/{course_id}",
            response_model = CourseResponse)
def update_course(course_id:int, updated_course: CourseCreate, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.title = updated_course.title
    course.description = updated_course.description 
    course.instructor = updated_course.instructor
    course.credits = updated_course.credits
    course.capacity = updated_course.capacity
    course.enrolled_count = updated_course.enrolled_count
    course.price = updated_course.price
    course.status = updated_course.status

    db.commit()
    db.refresh(course)

    return course
@router.delete("/{course_id}")
def delete_course(course_id: int,db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.course_id == course_id).first()
    if not course:
        raise HTTPException(status_code == 404,detail= "Course not found")
    db.delete(course)
    db.commit()

    return{"message":"Course deleted successfully"}
    