'''
In this file we will have reusable functions to interact with the data in the database.

CRUD comes from: Create, Read, Update, and Delete.
'''

from sqlalchemy.orm import Session # this will allow you to declare the type of the db parameters and have better type checks and completion in your functions.
from . import models, schemas # (SQLAlchemy models) and (the Pydantic models / schemas).
from fastapi import FastAPI , HTTPException

def create_a_student(db : Session , student:schemas.Student) :
    new_student = models.Student(fristname= student.firstname , lastname = student.lastname , average = student.average , graduated = student.graduated)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_student_info(db: Session , student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    return student


def show_database(db :Session , skip: int = 0):
    database = db.query(models.Student).offset(skip).all()
    return database


def delete_student(db:Session , student_id:int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None :
        raise HTTPException(status_code=404 , detail="student not found")
    db.delete(student)
    db.commit()
    return {"message" : "student deleted successfully"}


def edit_student_info(db:Session , student_id:int , edit_field:str , field_value:list[str,float,bool,int]):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if edit_field == "firstname" :
        student.firstname = field_value
    elif edit_field == "lastname" :
        student.lastname = field_value
    elif edit_field == "average" :
        student.average = field_value
    elif edit_field == "graduated" :
        student.graduated = field_value

    db.commit()
    db.refresh(student)
    return student

#----------------------------------------------

def create_student_course(db: Session , course: schemas.Course , student_id:int):
    st_course = models.Course(**course.model_dump() , owner_id=student_id)
    db.add(st_course)
    db.commit()
    db.refresh(st_course)
    return st_course



# def edit_course_info(db:Session , course_name:str ):
#     selected_course = db.query(models.Course).filter(models.Course.name == course_name).first()

#     if selected_course is None  : 
#         raise HTTPException(status_code=404 , detail="course not found")

#     if type(field_value) is str :
#         crud.edit_course_info()
#     elif type(field_value) is int :
#     if course_field == "name" :
#         stu_course.name = course_field_value
#     elif course_field == "unit" :
#         stu_course.unit = course_field_value



def show_all_courses(db:Session , skip:int=0 ):
    courses_db = db.query(models.Course).offset(skip).all()
    return courses_db

