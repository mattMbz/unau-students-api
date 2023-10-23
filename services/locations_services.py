from models.locations import Location as LocationModel
from schemas.locations import LocationSchema
from schemas.locations import LocationUpdateSchema
from schemas.locations import LocationName, LocationCountry


class LocationService():

    def __init__(self, db) -> None:
        self.db = db

    def getAll(self):
        result = self.db.query(LocationModel).all()
        return result

    def getLocationById(self, id):
        result = self.db.query(LocationModel).filter(
            LocationModel.id == id).first()
        return result

    def create(self, location: LocationSchema):
        # new_location = LocationModel(**location.model_dump()) # Esto solo si no hubiese un atributo Enum

        '''
            Debido a que hay un Atributo representado por una Clase tipo Enum el proceso es un poco mas largo
            porque debemos extraer el valor de ese Enum -> Ej: LocationName.posadas.value
        '''
        new_data = location.model_dump()
        for key, value in new_data.items():
            if key == "name":
                value = LocationName(value).value
                new_data[key] = value
            if key == "country":
                value = LocationCountry(value).value
                new_data[key] = value

        new_location = LocationModel(**new_data)
        self.db.add(new_location)
        self.db.commit()
        return

    def update(self, id, data):
        location = self.db.query(LocationModel).filter(LocationModel.id == id).first()
        new_data = data.model_dump()

        for key, value in new_data.items():
            if value is not None:
                if key == "name":
                    value = LocationName(value).value
                if key == "country":
                    value = LocationCountry(value).value
                setattr(location, key, value)


        self.db.commit()
        self.db.refresh(location)

        return location


    def updateAll(self, id: int, data: LocationSchema):
        return self.update(id, data)

    def updateData(self, id: int, data: LocationUpdateSchema):
        return self.update(id, data)

    def delete(self, id: int):
        self.db.query(LocationModel).filter(LocationModel.id == id).delete()
        self.db.commit()
        return
