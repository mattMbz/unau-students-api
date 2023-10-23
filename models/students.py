from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from models.many_to_many import (
    student_subject_association,
    student_studentProject_association,
    student_collegeCareer_association,
    student_extensionActivities_association
)

from models.subjects import Subject
from models.college_career import CollegeCareer
from models.student_projects import StudentProject
from models.extension_activities import ExtensionActivity
from models.library_debts import LibraryDebt


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=False)
    nationality = Column(String(15), nullable=False)
    dni = Column(String(12), unique=True, nullable=False)
    birth_date = Column(Date, nullable=False)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(50), nullable=True)
    matriculation = Column(Integer, nullable=True)

    # many-to-many relation with Subject
    subjects = relationship (
        Subject, 
        secondary=student_subject_association, 
        back_populates='students'
    )

    # many-to-one relation with Location
    location_id = Column(
        Integer,
        ForeignKey('locations.id', ondelete='RESTRICT'),
        unique=False,
        nullable=False
    )
    
    location = relationship('Location', back_populates="student")

    # many-to-many relation with StudentProject
    student_projects = relationship (
        StudentProject, 
        secondary=student_studentProject_association, 
        back_populates='students'
    )

    # many-to-many relation with CollegeCareer
    college_careers = relationship (
        CollegeCareer,
        secondary=student_collegeCareer_association,
        back_populates='students'
    )

    # many-to-many relations with ExtensionAtivity
    extension_activities = relationship(
        ExtensionActivity,
        secondary=student_extensionActivities_association,
        back_populates='students'
    )

    # one-to-many relation with LibraryDebt
    library_debts = relationship(LibraryDebt, back_populates="student")

    # one-to-one relation with Attendance
    attendance = relationship("Attendance", uselist=False, back_populates="student")