'''
In this file we will have reusable functions to interact with the data in the database.

CRUD comes from: Create, Read, Update, and Delete.
'''

from sqlalchemy.orm import Session # this will allow you to declare the type of the db parameters and have better type checks and completion in your functions.
from . import models, schemas # (SQLAlchemy models) and (the Pydantic models / schemas).
from fastapi import FastAPI , HTTPException

def create_a_student(db : Session , student:schemas.StudentCreate) :
    new_student = models.Student(firstname= student.firstname , lastname = student.lastname , average = student.average , graduated = student.graduated)
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
    stu = db.query(models.Student).filter(models.Student.id == student_id).first()
    if stu is None :
        raise HTTPException(status_code=404 , detail="student not found")
    db.delete(stu)
    db.commit()
    return {"message" : "student deleted successfully"}


def edit_student_info(db:Session , student_id:int ,field:str, new_value: str|int  , student: schemas.StudentCreate):
    selected_stu = db.query(models.Student).filter(models.Student.id == student_id).first()

    if field == "firstname" :
        selected_stu.firstname = new_value
    elif field == "lastname" :
        selected_stu.lastname = new_value
    elif field == "average" :
        selected_stu.average = new_value
    elif field == "graduated" :
        selected_stu.graduated == new_value 

    db.commit()
    db.refresh(selected_stu)
    return selected_stu

#----------------------------------------------

def create_student_course(db: Session , student_id:int ,course: schemas.Course ):
    st_course = models.Course(**course.model_dump() , owner_id=student_id)
    db.add(st_course)
    db.commit()
    db.refresh(st_course)
    return st_course

def get_course_info(db: Session , course_id: int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    return course

def show_all_courses(db:Session , skip:int=0 ):
    courses_db = db.query(models.Course).offset(skip).all()
    return courses_db

def edit_course_info(db:Session , course_id:int ,field:str, new_value: str|int  , course: schemas.CourseCreate):
    selected_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if field == "name" :
        selected_course.name = new_value
    elif field == "unit" :
        selected_course.unit = new_value
    elif field == "owner_id" :
        selected_course.owner_id = new_value
    db.commit()
    db.refresh(selected_course)
    return selected_course


def delete_course(db:Session , course_id:int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course is None :
        raise HTTPException(status_code=404 , detail="course not found")
    db.delete(course)
    db.commit()
    return {"message" : "course deleted successfully"}






