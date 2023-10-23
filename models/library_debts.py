from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
# from models.students import Student

class LibraryDebt(Base):

    __tablename__ = "library_debts"
    
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(String(10))
    state = Column(String(15))
    delivery_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)

    # We define the many-to-one relationship with 'students' model
    student_id = Column(
        Integer,
        ForeignKey('students.id', ondelete='SET NULL'),
        unique = False
    )

    # many-to-one relationships with Student
    student = relationship('Student', back_populates="library_debts")