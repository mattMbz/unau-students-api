from config.database import Base
from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from models.many_to_many import subjects_grades_association


class Grade(Base):

    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Float)


    subjects = relationship (
        'Subject',
        secondary=subjects_grades_association,
        back_populates='grades'
    )