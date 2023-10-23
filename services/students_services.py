import random
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from models.students import Student as StudentModel
from schemas.students import StudentSchema
from schemas.students import StudentUpdateSchema
from schemas.locations import LocationNumber


class StudentService():

    def __init__(self, db) -> None:
        self.db = db

    def getAll(self):
        result = self.db.query(StudentModel).all()
        return result

    def getStudentById(self, id):
        result = self.db.query(StudentModel).filter(StudentModel.matriculation == id).first()
        if not result:
            result = []
        return result

    # def getStudentByLocation(self, location: Location):
    #     pass

    def create(self, student: StudentSchema):
        # new_student = StudentModel(**student.model_dump())
        new_data = student.model_dump()
        for key, value in new_data.items():
            if key == "location_id":
                locationEnumValue =  LocationNumber(value).value
                print(f"encontrado {key} en {locationEnumValue}")
                new_data[key] = locationEnumValue #update dictionary with locationNumber value
                print(new_data)
            if key == "birth_date":
                str_date = new_data['birth_date']
                python_date = datetime.strptime(str_date, "%Y-%m-%d").date()
                new_data[key] = python_date
        
        new_data['matriculation'] = random.randint(1000, 50000)
        new_student = StudentModel(**new_data)
        try:
            self.db.add(new_student)
            self.db.commit()
        except IntegrityError as err:
            self.db.rollback()
            print(err)
            raise err


    def update(self, id, data):
        student = self.db.query(StudentModel).filter(StudentModel.matriculation == id).first()
        new_data = data.model_dump()
        for key, value in new_data.items():
            if value is not None:
                if key == "location_id":
                    locationEnumValue =  LocationNumber(value).value
                    value = locationEnumValue #update dictionary with locationNumber value
                if key == "birth_date":
                    str_date = new_data['birth_date']
                    value = datetime.strptime(str_date, "%Y-%m-%d").date()
                
                setattr(student, key, value)

        self.db.commit()
        self.db.refresh(student)

        return student

    def updateAll(self, id: int, data: StudentSchema):
        return self.update(id, data)

    def updateData(self, id: int, data: StudentUpdateSchema):
        return self.update(id, data)

    def delete(self, id: int):
        self.db.query(StudentModel).filter(StudentModel.matriculation == id).delete()
        self.db.commit()
        return
