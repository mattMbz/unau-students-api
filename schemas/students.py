from typing import Optional
from datetime import datetime
from .locations import LocationNumber
from pydantic import BaseModel, Field, EmailStr, validator
from pydantic_extra_types.phone_numbers import PhoneNumber


PhoneNumber.phone_format = 'E164'

class StudentSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=20)
    last_name: str = Field(min_length=1, max_length=20)
    nationality: str = Field(min_length=3, max_length=15)
    dni: str = Field(min_length=8, max_length=12)
    birth_date: str = Field(
        title="Student birth date",
        description="Student birth date on ISO 8601 standard, with format 'YYYY-MM-DD'",
        example="2002-06-20"
    )
    location_id: LocationNumber
    phone_number: PhoneNumber
    email: EmailStr

    @validator("first_name", "last_name")
    def validate_empty_files(cls, value):
        '''Check if the value is blank or contains only whitespace'''
        if not value.strip():
            raise ValueError("The 'first_name' field cannot be blank or contain only whitespace")
        return value

    @validator("birth_date")
    def validate_birth_date(cls, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("The date must be in the format 'YYYY-MM-DD'")

        return value
    

    class Config:
        json_schema_extra = {
            "example": {
                "first_name" : "Facundo",
                "last_name": "Garcia Martoni",
                "nationality": "Argentina",
                "phone_number": "+54-3755-265654",
                "dni": "40789563",
                "birth_date": "2001-11-05",
                "email": "facundo.martoni@xmail.com",
                "location_id": 1
            }
        }


class StudentUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(default=None, min_length=1, max_length=20)
    last_name: Optional[str] = Field(default=None, min_length=1, max_length=20)
    nationality: Optional[str] = Field(default=None, min_length=3, max_length=15)
    dni: Optional[str] = Field(default=None, min_length=8, max_length=12)
    birth_date: Optional[str] = Field(default=None)
    location_id: Optional[LocationNumber] = Field(default=None)
    phone_number: Optional[PhoneNumber] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "first_name" : "Facundo",
                "last_name": "Garcia Martoni",
                "nationality": "Argentina",
                "phone_number": "+54-3755-265654",
                "dni": "40789563",
                "birth_date": "2001-11-05",
                "email": "facundo.martoni@xmail.com",
                "location_id": 1
            }
        }