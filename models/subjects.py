from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.many_to_many import (
    student_subject_association,
    subjects_grades_association,
    subjects_college_careers_association
)
from models.grades import Grade
from models.college_career import CollegeCareer
from models.attendance import Attendance

class Subject(Base):

    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(120), nullable=True)

    # Establecer la relación many-to-many con Student
    students = relationship (
        'Student', 
        secondary=student_subject_association, 
        back_populates='subjects'
    )

    grades = relationship (
        Grade,
        secondary=subjects_grades_association,
        back_populates='subjects'
    )

    college_careers = relationship (
        CollegeCareer,
        secondary=subjects_college_careers_association,
        back_populates='subjects'
    )

    attendances = relationship (
        Attendance, 
        back_populates="subjects"
    )
