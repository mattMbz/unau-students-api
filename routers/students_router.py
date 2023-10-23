from fastapi import APIRouter
from fastapi import status, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.students_services import StudentService as Services
from schemas.students import StudentSchema
from schemas.students import StudentUpdateSchema
from models.students import Student
from sqlalchemy.exc import IntegrityError


students_router = APIRouter()


@students_router.get(path='/students', tags=['Students'])
def get_students():
    db = Session()
    students = Services(db).getAll()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(students)
    )


@students_router.get(path='/students/{id}', tags=['Students'])
def get_student_by_id(id: int = Path(ge=1000, le=1000000)):
    db = Session()
    student = Services(db).getStudentById(id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(student)
    )


@students_router.post(path='/students', tags=['Students'])
def create_new_student(student: StudentSchema):
    try:
        db = Session()
        Services(db).create(student)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=jsonable_encoder({"message": "New Student has been created succesfully"})
        )
    except IntegrityError as err:
        db.rollback()
        error_message = f"Error: {str(err)}"
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": error_message[0:70]}
        )


@students_router.put(path='/students/{id}', tags=['Students'])
def update_student_all_data(id: int, data: StudentSchema):
    db = Session()
    result = Services(db).updateAll(id, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"content": result})
    )


@students_router.patch(path='/students/{id}', tags=['Students'])
def update_student_data(id: int, data: StudentUpdateSchema):
    db = Session()
    result = Services(db).updateData(id, data)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"content": result})
    )


@students_router.delete(path='/students/{id}', tags=['Students'])
def delete_student(id: int):
    db = Session()
    result = db.query(Student).filter(Student.matriculation == id).first()

    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Not Found"}
        )
    
    Services(db).delete(id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": f"Se ha eliminado al alumno {result.first_name} - {result.matriculation}"}
    )
