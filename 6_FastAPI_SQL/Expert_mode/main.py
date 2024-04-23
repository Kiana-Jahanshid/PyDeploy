from sqlalchemy.orm import Session # this will allow you to declare the type of the db parameters and have better type checks and completion in your functions.
from . import models, schemas , crud # (SQLAlchemy models) and (the Pydantic models / schemas).
from fastapi import FastAPI , HTTPException , Depends
from .database import SessionLocal, Engine


models.Base.metadata.create_all(bind=Engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()


@app.post("/add_student/{fname}/{lname}/{average}/{graduated}" , response_model=schemas.Student)
def create_a_student(student:schemas.StudentBase ,fname :str , lname:str , average:float , graduated:bool, db: Session=Depends(get_db) ) :
    student.firstname = fname
    student.lastname = lname
    student.average = average
    student.graduated = graduated
    new_student = crud.create_a_student(db=db , student=student)
    return new_student


@app.get("/get_student/{student_id}" , response_model=schemas.Student)
def show_a_student_info(student_id: int , db: Session=Depends(get_db) ):
    student_info = crud.get_student_info(db=db , student_id=student_id)
    if student_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return student_info


@app.get("/show_database/" , response_model=list[schemas.Student])
def show_database(db :Session=Depends(get_db) , skip: int = 0):
    database = crud.show_database(db=db , skip=skip)
    return database


@app.put("/edit_student/{student_id}/{field}/{new_vlaue}" , response_model=schemas.Student)
def edit_student_info(student_id:int ,field:str, new_value: str|int ,  student:schemas.Student ,db:Session=Depends(get_db) ):
    stu = crud.get_student_info(db=db , student_id=student_id)
    if stu is None :
        raise HTTPException(status_code=404 , detail="student not found")
    edited_student = crud.edit_student_info(db=db , student_id=student_id , student=student , field=field , new_value=new_value)
    return edited_student


@app.delete("/delete_student/{student_id}" )
def delete_student(student_id:int , db:Session=Depends(get_db) ):   
    message = crud.delete_student(db=db , student_id=student_id )
    return message



#---------------------------------------------------------------------------------


@app.post("/add_student_course/{student_id}/{course_name}/{course_unit}", response_model=schemas.Course)
def create_course_for_student(student_id:int ,course_name:str , course_unit:int , course: schemas.CourseCreate , db: Session = Depends(get_db)):
    course.name = course_name
    course.unit = course_unit
    new_course = crud.create_student_course(db=db, course=course , student_id=student_id) 
    return new_course


@app.get("/show_all_courses/" , response_model=list[schemas.Course])
def show_courses(db :Session=Depends(get_db) , skip: int = 0):
    courses_db = crud.show_all_courses(db=db , skip=skip)
    return courses_db


@app.put("/edit_course/{course_id}/{field}/{new_vlaue}" , response_model=schemas.Course)
def edit_course_info(course_id:int ,field:str, new_value: str|int ,  course:schemas.Course ,db:Session=Depends(get_db) ):
    edit_course = crud.get_course_info(db=db , course_id=course_id)
    if edit_course is None :
        raise HTTPException(status_code=404 , detail="student not found")
    edited_course = crud.edit_course_info(db=db , course_id=course_id , course=course , field=field , new_value=new_value)
    return edited_course


@app.delete("/delete_course/{course_id}" )
def delete_course(course_id:int , db:Session=Depends(get_db) ):   
    message = crud.delete_course(db=db , course_id=course_id )
    return message