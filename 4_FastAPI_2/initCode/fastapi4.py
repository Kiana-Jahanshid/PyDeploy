from typing import Union
from fastapi import FastAPI , Form , File , UploadFile , HTTPException
from pydantic import BaseModel
from fastapi.responses import StreamingResponse 
import cv2
import io 
import numpy as np


# upgrading last example 
# adding some another requests , except get 
# ---------------------------------------------
# for using HTTP methods like post , put , delete
# we need a database to store data
# to apply these methods 

app = FastAPI()

database = {}


@app.get("/")
def read_root():
    return {"hello" : "world"}


@app.get("/items")
def reading_db_items():
    return database


# these 3 info parameter , should pass using Form()
@app.post("/items")
def adding_db_an_item(id_number:str = Form(), person_name :str = Form() , age: float=Form()):
    database[id_number] = {"name" :person_name , "age" :age}
    return database[id_number]

# here we have same endpoints "/items" with different method types (post & get)
# in "browser address bar" , we only can use get method (not post method)
@app.delete("/items/delete_item/{id}")
def delete_an_item(id :str):
    # check item 
    if id not in database :
        raise HTTPException(status_code=404 , detail="item not found")
    else:
        del database[id]
    return "item has been deleted"


# update an item in DB
@app.put("/update/item/{id}") 
def update_an_item(id:str , name:str=Form(None) , age:float=Form(None)):
    #search item
    if id not in database:
        raise HTTPException(status_code=404 , detail="item not found")
    else:
        if name is not None : # if we have a new name
            database[id]["name"] = name
        if age is not None :
            database[id]["age"] = age

    return database[id]


#--------------------------------------------------------
# get/receive an image from user , and send it to api
'''
in postman :
POSt --> http://127.0.0.1:8000/rgb2gray 
Body --> key = input_file , value = file (upload a file)

----------------------------
async / await :
we use these , when the process will takes few seconds .

'''
@app.post("/rgb2gray")
async def rgb_to_gray(input_file: UploadFile=File(None)):

    # check input file type
    # if is not image
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415 , detail="unknown file type - type error")
    else :
        file_content = await input_file.read() # reading file may takes few seconds
        nparr = np.frombuffer(file_content , dtype=np.uint8)
        # unchanged : means if image is png , do not convert it to jpg 
        # and keep it transparent 
        decoded_image = cv2.imdecode(nparr , cv2.IMREAD_UNCHANGED)

        gray_image = cv2.cvtColor(decoded_image , cv2.COLOR_BGR2GRAY)
        _ , encoded_image = cv2.imencode(".jpg" , img=gray_image)
        image_bytes = encoded_image.tobytes()
        final_image = io.BytesIO(image_bytes)
        return StreamingResponse(final_image, media_type= "image/jpeg")

