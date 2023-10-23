from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class LocationCountry(Enum):
    argentina: str = "Argentina"
    bolivia: str = "Bolivia"
    brasil: str = "Brasil"
    chile: str = "Chile"
    colombia: str = "Colombia"
    ecuador: str = "Ecuador"
    guyana: str = "Guyana"
    paraguay: str = "Paraguay"
    peru: str = "Perú"
    surinam: str = "Surinam"
    uruguay: str = "Uruguay"
    venezuela: str = "Venezuela"

class LocationNumber(Enum):
    posadas: int = 1
    obera: int = 2
    eldorado: int = 3
    san_vicente: int = 4
    dos_de_mayo: int = 5

class LocationName(Enum):
    posadas: str = "Posadas"
    obera: str = "Oberá"
    eldorado: str = "Eldorado"
    san_vicente: str = "San Vicente"
    dos_de_mayo: str = "Dos de mayo"


class LocationSchema(BaseModel):
    name: LocationName
    address: str = Field(min_length=1, max_length=50)
    province: str = Field(min_length=1, max_length=50)
    country: LocationCountry

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Posadas",
                "address": "Catamarca 1921",
                "province": "Misiones",
                "country": "Argentina"
            }
        }


class LocationUpdateSchema(BaseModel):
    name: Optional[LocationName] = Field(default=None)
    address: str = Field()
    province: Optional[str] = Field(default=None, min_length=1, max_length=20)
    country: Optional[LocationCountry] = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Posadas",
                "address": "Catamarca 1921",
                "province": "Misiones",
                "country": "Argentina"
            }
        }
