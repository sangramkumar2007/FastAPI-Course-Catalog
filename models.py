from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key = True, index =True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    instructor = Column(String(100))
    credits = Column(Integer)
    capacity = Column(Integer)
    enrolled_count= Column(Integer)
    price = Column(Integer)
    status = Column(String(20))
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__ = "enrollments"
    enrollment_id = Column(Integer, primary_key=True,index=True)
    student_name = Column(String(100), nullable=False)
    student_email = Column(String(100), nullable= False)
    enrollment_date = Column(String(50))
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    course = relationship("Course")