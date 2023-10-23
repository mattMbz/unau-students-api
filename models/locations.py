from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Location(Base):

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False, unique=True)
    address = Column(String(20), nullable=False)
    province = Column(String(20), nullable=False)
    country = Column(String(20), nullable=False)

    # Definir la relación inversa
    student = relationship('Student', back_populates="location")
