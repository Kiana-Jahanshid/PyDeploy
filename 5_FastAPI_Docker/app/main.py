from fastapi import FastAPI , Form , File , UploadFile , HTTPException
from fastapi.responses import StreamingResponse , FileResponse
import sqlite3


app = FastAPI()

#create a connection to an SQLite database:
def create_connection():
    connection = sqlite3.connect("todo.db")
    return connection

def print_db(cursor):
    db_rows= []
    for row in cursor.execute("SELECT id,title , description , time , status from TASKS"):
        db_rows.append({"id" : f"{row[0]}" , "title": f"{row[1]}" , "description": f"{row[2]}", "time": f"{row[3]}", "status": f"{row[4]}"})
    return db_rows


@app.get("/read_db")
def read_database():
    connection = create_connection()
    cursor = connection.cursor()
    database = print_db(cursor)
    connection.close()
    return database


@app.post("/add_task/{id}/{title}/{description}/{time}/{status}")
def add_a_task(id:int , title:str , description:str , time:str , status:int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM TASKS WHERE id = '{id}' ")
    occurrence_number = cursor.fetchall()
    if  len(occurrence_number) > 0 :
        raise HTTPException(status_code=400 , detail="this id number is already exists in database , try another id ")        
    else :    
        cursor.execute("INSERT INTO TASKS (id , title , description , time , status) VALUES (?,?,?,?,?)" , (id , title , description , time , status))       
        connection.commit()
        database = print_db(cursor)
        connection.close()
        return database
    

@app.put("/update_task/{id}/{field_name}/{new_field_value}")
def update_a_task(id:int , field_name:str , new_field_value:str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM TASKS WHERE id = '{id}' ")
    occurrence_number = cursor.fetchall()
    if  len(occurrence_number) < 1 :
        raise HTTPException(status_code=400 , detail="this id does not exists in database , try another id ")        
    else :
        cursor.execute(f"UPDATE TASKS SET {field_name} = '{new_field_value}' WHERE id = '{id}'")
        connection.commit()
        database = print_db(cursor)
        connection.close()
        return database


@app.delete("/delete_task/{id}")
def delete_a_task(id:int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * from TASKS WHERE id = '{id}' ")
    occurrence_number = cursor.fetchall()
    if len(occurrence_number) == 0 :
        raise HTTPException(status_code=400 , detail="Task Can not be deleted , because this id does not exists in database")
    else :
        cursor.execute(f"DELETE from TASKS WHERE id = {id}")
        connection.commit()
        database = print_db(cursor)
        connection.close()
        return database  
