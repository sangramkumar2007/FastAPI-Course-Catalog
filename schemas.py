from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str
    instructor: str
    credits: int
    capacity: int
    enrolled_count: int
    price: int
    status: str

class CourseCreate(CourseBase):
    pass
class CourseUpdate(CourseBase):
    pass
class CourseResponse(CourseBase):
    course_id: int
    class Config:
        from_attributes = True

class EnrollmentBase(BaseModel):
    student_name: str
    student_email:  str
    enrollment_date:  str
    course_id: int
class EnrollmentCreate(EnrollmentBase):
    pass
class EnrollmentResponse(EnrollmentBase):
    enrollment_id: int
    class Config:
        from_attributes = True