from config.database import Base
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
# from models.subjects import Subject

class Attendance(Base):

    __tablename__ = "attendances"
    
    id = Column(Integer, primary_key=True, index=True)
    state = Column(String(10))
    date = Column(Date)

    # Campo que hace referencia al estudiante (one-to-one)
    student_id = Column(Integer, ForeignKey('students.id'), unique=True)
    
    # Relación one-to-one con Student
    student = relationship("Student", back_populates="attendance")

    subject_id = Column(
        Integer,
        ForeignKey('subjects.id', ondelete='SET NULL'),
        unique=False
    )
    
    subjects = relationship("Subject" , back_populates="attendances")