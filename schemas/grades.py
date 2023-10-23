from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class ValueEnum(int, Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10


class GradeSchema(BaseModel):
    value: ValueEnum

    class Config:
        json_schema_extra = {
            "example": {
                "value": 7
            }
        }


class GradeUpdateSchema(BaseModel):
    value: Optional[ValueEnum] = Field(default=None)
    
    class Config:
        json_schema_extra = {
            "example": {
                "value": 7
            }
        }