from fastapi import APIRouter
from fastapi import status, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from schemas.locations import LocationSchema
from schemas.locations import LocationUpdateSchema
from services.locations_services import LocationService as Services
from models.locations import Location

locations_router = APIRouter()


@locations_router.get('/locations', tags=['Locations'])
def get_all_locations():
    db = Session()
    result = Services(db).getAll()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )


@locations_router.get('/locations/{id}', tags=['Locations'])
def get_location_by_id(id: int = Path(ge=1, le=100)):
    db = Session()
    result = Services(db).getLocationById(id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )


@locations_router.post('/locations', tags=['Locations'], status_code=status.HTTP_201_CREATED)
def create_new_location(location: LocationSchema):
    db = Session()
    Services(db).create(location)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {"message": "New location has been created succesfully"})
    )


@locations_router.put('/locations/{id}', tags=['Locations'])
def update_location_all_data(id: int, data: LocationSchema):
    db = Session()
    result = Services(db).updateAll(id, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"content": result})
    )


@locations_router.patch('/locations/{id}', tags=['Locations'])
def update_location_data(id: int, data: LocationUpdateSchema):
    db = Session()
    result = Services(db).updateData(id, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"content": result})
    )


@locations_router.delete('/locations/{id}', tags=['Locations'])
def delete_location(id: int):
    db = Session()
    result = db.query(Location).filter(Location.id == id).first()

    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Not Found"}
        )

    Services(db).delete(id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": f"Se ha eliminado la Localidad de {result.name}"}
    )
