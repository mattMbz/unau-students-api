from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator


class StudentProjectSchema(BaseModel):
    project_name: str = Field(min_length=10, max_length=100)
    description: str = Field(min_length=20, max_length=1024)
    date: str = Field(
        title="Student Project date",
        description="Student Project date with format YYYY-MM-DD",
        example="2020-06-20"
    )
    conference_id: int = Field(gt=0)

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
                "project_name": "AgroInnovación Verde: Investigación para una agricultura y ganadería sostenibles en el siglo XXI.",
                "description": "AgroInnovación Verde es un proyecto interdisciplinario que busca revolucionar la agricultura y la ganadería, promoviendo prácticas sostenibles, la conservación de recursos y la eficiencia energética para asegurar la prosperidad agrícola y la preservación del medio ambiente en el siglo XXI.",
                "date": "2021-07-15",
                "conference_id": 12
            }
        }


class StudentProjectUpdateSchema(BaseModel):
    project_name: Optional[str] = Field()
    description: Optional[str] = Field()
    date: Optional[str] = Field()
    conference_id: Optional[int] = Field()

    class Config:
        json_schema_extra = {
            "example": {
                "project_name": "AgroInnovación Verde: Investigación para una agricultura y ganadería sostenibles en el siglo XXI.",
                "description": "AgroInnovación Verde es un proyecto interdisciplinario que busca revolucionar la agricultura y la ganadería, promoviendo prácticas sostenibles, la conservación de recursos y la eficiencia energética para asegurar la prosperidad agrícola y la preservación del medio ambiente en el siglo XXI.",
                "date": "2021-07-15",
                "conference_id": 12
            }
        }