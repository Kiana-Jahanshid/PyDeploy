from sqlalchemy.orm import Session # this will allow you to declare the type of the db parameters and have better type checks and completion in your functions.
import models, schemas , crud # (SQLAlchemy models) and (the Pydantic models / schemas).
from fastapi import FastAPI , HTTPException , Depends
from database import SessionLocal, Engine



models.Base.metadata.create_all(bind=Engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()



@app.post("/add_student" , response_model=schemas.Student)
def create_a_student(student:schemas.Student , db: Session=Depends(get_db) ) :
    check_student = crud.get_student_info(db=db , student_id=student.id)
    if check_student is not None :
        raise HTTPException(status_code=404 , detail="student is already existed in db")
    new_student = crud.create_a_student(db=db , student=student)
    return new_student


@app.get("/student/{student_id}" , response_model=schemas.Student)
def show_a_student_info(student_id: int , db: Session=Depends(get_db) ):
    student_info = crud.get_student_info(db=db , student_id=student_id)
    if student_info is None:
        raise HTTPException(status_code=404, detail="User not found")
    return student_info


@app.get("/show_database" , response_model=list[schemas.Student])
def show_database(db :Session=Depends(get_db) , skip: int = 0):
    database = crud.show_database(db=db , skip=skip)
    return database


@app.put("/edit_student/{student_id}/{field}/{new_field_value}" , response_model=schemas.Student)
def edit_student(student_id:int ,field:str , new_field_value:list[str,float,bool,int] ,db:Session=Depends(get_db) ):
    stu = crud.get_student_info(db=db , student_id=student_id)
    if stu is None :
        raise HTTPException(status_code=404 , detail="student not found")
    edited_student = crud.edit_student_info(db=db , student_id=student_id , edit_field=field , field_value=new_field_value)
    return edited_student




@app.delete("/delete_student/{student_id}" , response_model=schemas.Student)
def delete_student(student_id:int , db:Session=Depends(get_db) ):   
    return crud.delete_student(db=db , student_id=student_id)

#---------------------------------------------------------------------------------



@app.post("/add_student_course/{student_id}/courses/", response_model=schemas.Course)
def create_course_for_student(student_id: int, course: schemas.Course, db: Session = Depends(get_db)):
    new_course = crud.create_student_course(db=db, course=course, student_id=student_id) 
    return new_course


@app.get("/show_courses" , response_model=list[schemas.Course])
def show_courses(db :Session=Depends(get_db) , skip: int = 0):
    courses_db = crud.show_all_courses(db=db , skip=skip)
    return courses_db