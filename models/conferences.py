from config.database import Base
from sqlalchemy import Table, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Conference(Base):

    __tablename__ = "conferences"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    date = Column(Date)

    student_projects = relationship (
        "models.student_projects.StudentProject", 
        back_populates="conferences"
    )