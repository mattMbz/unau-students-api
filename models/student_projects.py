from config.database import Base
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from models.many_to_many import student_studentProject_association
from models.conferences import Conference

class StudentProject(Base):

    __tablename__ = "student_projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100))
    description = Column(String(1024))
    date = Column(Date)

    students = relationship (
        'Student', 
        secondary=student_studentProject_association, 
        back_populates='student_projects'
    )

    conferences_id = Column(
        Integer,
        ForeignKey("conferences.id", ondelete='CASCADE'),
        unique=False
    )

    conferences = relationship(Conference, back_populates="student_projects")
