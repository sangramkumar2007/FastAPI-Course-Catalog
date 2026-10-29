from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Enrollment
from schemas import EnrollmentCreate, EnrollmentResponse

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",response_model = EnrollmentResponse)
def create_enrollment(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    new_enrollment = Enrollment(
        student_name= enrollment.student_name,
        student_email = enrollment.student_email,
        enrollment_date = enrollment.enrollment_date,
        course_id = enrollment.course_id
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)

    return new_enrollment
@router.get("/",
            response_model=list[EnrollmentResponse]
            )
def get_enrollments(db: Session = Depends(get_db)):
    enrollments = db.query(Enrollment).all()
    return enrollments

@router.get("/{enrollment_id}",response_model= EnrollmentResponse)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()

    if not enrollment:
        raise HTTPException(
            status_code = 404,
            detail = "Enrollment not found"
        )
    return enrollment

@router.put("/{enrollment_id}", response_model = EnrollmentResponse)
def update_enrollment(
    enrollment_id: int,
    updated_enrollment: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    enrollment = db.query(Enrollment).filter(Enrollment.enrollment_id == enrollment_id).first()
    if not enrollment:
        raise HTTPException(
            status_code =404,
            detail= "Enrollment not found"
        )
    enrollment.student_name = updated_enrollment.student_name
    enrollment.student_email = updated_enrollment.student_email
    enrollment.enrollment_date = updated_enrollment.enrollment_date
    enrollment.course_id = updated_enrollment.course_id

    db.commit()
    db.refresh(enrollment)

    return enrollment

@router.delete("/{enrollment_id}")
def delete_enrollment(
    enrollment_id:int,
    db: Session = Depends(get_db)
):
    enrollment = db.query(Enrollment).filter(
        Enrollment.enrollment_id == enrollment_id
    ).first()
    if not enrollment:
        raise HTTPException(
            status_code = 404,
            detail = "Enrollment not found"
        )
    db.delete(enrollment)
    db.commit()

    return{"message": "Enrollment deleted successfully"}