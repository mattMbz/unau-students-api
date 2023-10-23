from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator


class ConferenceSchema(BaseModel):
    name: str = Field()
    description: str = Field(min_length=10, max_length=250)
    date: str = Field( 
        name= "Date for a conference",
        description= "Date in YYYY-MM-DD format",
        example= "2021-07-12"
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
                "name":"XXI Congreso Argentino de Medicina y Nutrición",
                "description": "Congreso asistido por UNAU, con presentación de 3 proyectos. Universidad de Buenos Aires",
                "date": "2021-07-12",
            }
        }


class ConferenceUpdateSchema(BaseModel):
    name: Optional[str] = Field()
    description: Optional[str] = Field()
    date: Optional[str] = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "name":"XXI Congreso Argentino de Medicina y Nutrición",
                "description": "Congreso asistido por UNAU, con presentación de 3 proyectos. Universidad de Buenos Aires",
                "date": "2021-07-12",
            }
        }