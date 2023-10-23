from typing import Optional
from pydantic import BaseModel, Field, validator


class SubjectSchema(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    description: str = Field(min_length=5, max_length=100)

    @validator("name", "description")
    def validate_empty_files(cls, value):
        '''Check if the value is blank or contains only whitespace'''
        if not value.strip():
            raise ValueError("The field cannot be blank or contain only whitespace")
        return value
    
    class Config:
        json_schema_extra = {
            "example" : {
                "name": "Investigación Operativa I",
                "description": "Cátedra correspondiente a LAN"
            }
        }


class SubjectUdateSchema(BaseModel):
    name: Optional[str] = Field(default=None, min_length=3, max_length=20)
    description: Optional[str] = Field(default=None, min_length=5, max_length=100)

    class Config:
        json_schema_extra = {
            "example" : {
                "name": "Investigación Operativa I",
                "description": "Cátedra correspondiente a LAN"
            }
        }