from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator

class ExtensionActivitySchema(BaseModel):
    name: str = Field(min_length=5, max_length=100)
    description: str = Field(min_length=0, max_length=500)
    date: str = Field(
        title='Extension activity',
        description="Student extra extension activity with date in 'YYYY-MM-DD' format",
        example='2021-07-12'
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
            "example": {
                "title":"Jornadas sobre Orientación vocacional UNAU",
                "description": "Jornadas sobre orientación vocacional para alumnos de Licenciatura en Nutrición",
                "date": "2021-07-12",
            }
        }

class ExtensionActivityUpdateSchema(BaseModel):
    name: Optional[str] = Field()
    descrition: Optional[str] = Field()
    date: Optional[str] = Field(default=None)
    
    class Config:
        json_schema_extra = {
            "example": {
                "title":"Jornadas sobre Orientación vocacional UNAU",
                "description": "Jornadas sobre orientación vocacional para alumnos de Licenciatura en Nutrición",
                "date": "2021-07-12",
            }
        }