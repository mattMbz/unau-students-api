from typing import Optional
from pydantic import Field, BaseModel


class CollegeCareerSchema(BaseModel):
    name: str = Field(min_length=20, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Técnico Universitario en Desarrollo Agropecuario"
            }
        }

class CollegeCareerUpdateSchema(BaseModel):
    name: Optional[str] = Field()
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Técnico Universitario en Desarrollo Agropecuario"
            }
        }
