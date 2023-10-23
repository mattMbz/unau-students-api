from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from enum import Enum


class StateEnum(str, Enum):
    PRESENT = 'P'
    ABSENT = 'A'


class AttendanceSchema(BaseModel):
    state: StateEnum
    student_id: int
    subject_id: int
    date: str = Field(
        title="Student Attendance Date",
        description="Attendance date with format 'YYYY-MM-DD'",
        example="2002-06-20"
    )

    @validator("date")
    def validate_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("The date must be in the format 'YYYY-MM-DD'")

        return value

    class Config:
        json_schema_extra = {
            "example" : {
                "state": "P",
                "date": "2022-05-05",
                "student_id": 5657,
                "subject_id": 3
            }
        }


class AttendanceUpdateSchema(BaseModel):
    state: Optional[StateEnum] = Field(default=None)
    student_id: Optional[int] = Field()
    subject_id: Optional[int] = Field()
    date: Optional[str] = Field()
    
    class Config:
        json_schema_extra = {
            "example" : {
                "state": "P",
                "date": "2022-05-05",
                "student_id": 5657,
                "subject_id": 3
            }
        }