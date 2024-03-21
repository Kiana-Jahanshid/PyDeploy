from typing import Union
from fastapi import FastAPI , HTTPException , status
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "world"}

# if we wnt to send a parameter to method , we should use it , in both 
# url's template in decorator and function 

# UNION
# sometimes the parameters we want to send , can have different types
@app.get("/items/{item_id}")
def read_item(item_id:int , q:Union[str , None] = None):
    return {"item_id": item_id , "q":q}

# name parameter can have both string and integer types :
@app.get("/tv-channel/{name}")
def test_func(name : Union[str , int]):
    return {"name" : name}

@app.get('/salam')
def func():
    return "aleik"

@app.get("/salam bar to/{name}")
def func2(name):
    return "aleyik salam " + name + " " + " jan"

@app.get("/salam/{firstname}/{lastname}")
def func3(firstname: str , lastname: str ):
    return "aleyik salam " + firstname +" " + lastname + " janan"


@app.get("/salam/{firstname}")
def func4(firstname: str , lastname: str = "lastname"): # here lastname is optional
    return "aleyik salam " + firstname +"\t" + lastname + " joon"



# return an image 
@app.get("/create-image/{red}/{green}/{blue}")
def image(red: int , green:int , blue:int):
    #validtion
    if 0 <=red<= 255 and  0<=green<=255  and 0<=blue<=255 :
        image = np.zeros((300 , 300, 3) , dtype=np.uint8)
        image[: , :] = (red , green , blue)
        image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
        cv2.imwrite("t.jpg" , image)
        # api is working , but the output will save in server and doesnt show to client/user

        #here we cant return image bc its a numpy array
        # we should encode it into a format that can be transfer by API
        _  , encoded_image = cv2.imencode(".png" , img= image)
        final_image = io.BytesIO(encoded_image.tobytes())

        return StreamingResponse(final_image, media_type= "image/png")
    
    else :
        # we SHOULDNT RETURN HTTPException
        #WE SHOULD RAISE IT , so that postman return another status code except 200
        # اگر از ریترن استفاده کنیم توی خروجی ۴۰۰ برمیگردونه ولی پستمن همچنان ۲۰۰ برمیگردونه
        # پس برای اینکه پستمن هم استاتوس غیر ۲۰۰ برگردونه از ریز استفاده میکنیم
        # the status will be : 400 bad request
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail="Numbers must be between 0 to 255")
    




    