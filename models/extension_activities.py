from config.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from models.many_to_many import student_extensionActivities_association

class ExtensionActivity(Base):

    __tablename__ = "extension_activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    date = Column(Date)

    students = relationship(
        'Student',
        secondary=student_extensionActivities_association,
        back_populates='extension_activities'
    )