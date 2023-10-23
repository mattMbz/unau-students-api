from typing import Optional
from pydantic import BaseModel, Field, validator
from enum import Enum
from datetime import datetime


class StateEnum(str, Enum):
    PENDING = "pendiente"
    RETURNED = "devuelto"
    OVERDUE = "vencido"


class LibraryDebtsSchema(BaseModel):
    book_id: int
    state: StateEnum
    delivery_date: str = Field(
        title="Date of book delivery",
        description="Date in ISO 8601 Standard",
        example="2022-12-22"
    )
    student_id: int

    @validator("delivery_date")
    def validate_delivery_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("The date must be in the format 'YYYY-MM-DD'")

        return value


    class Config:
        json_schema_extra = {
            "example": {
                "book_id": 11,
                "state":"devuelto",
                "delivery_date": "2022-10-20",
                "student_id": 2345
            }
        }


class LibraryDebtsUpdateSchema(BaseModel):
    book_id: Optional[int] = Field()
    state: Optional[StateEnum] = Field(default=None)
    delivery_date: Optional[str] = Field()
    student_id: Optional[int] = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "book_id": 11,
                "state":"devuelto",
                "delivery_date": "2022-10-20",
                "student_id": 2345
            }
        }