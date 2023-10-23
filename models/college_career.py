from config.database import Base
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from models.many_to_many import (
    student_collegeCareer_association,
    subjects_college_careers_association
)

class CollegeCareer(Base):

    __tablename__ = "college_careers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    students = relationship (
        'Student',
        secondary=student_collegeCareer_association,
        back_populates='college_careers'
    )

    subjects = relationship (
        'Subject',
        secondary=subjects_college_careers_association,
        back_populates='college_careers'
    )