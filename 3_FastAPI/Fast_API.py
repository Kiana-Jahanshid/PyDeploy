import os
from typing import Union 
from fastapi import FastAPI , HTTPException , status , Response , Request
from fastapi.responses import HTMLResponse , FileResponse , StreamingResponse
import cv2
import numpy as np
import io
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



app = FastAPI()
app.mount("/static", StaticFiles(directory="static" ))

@app.get("/" , response_class=HTMLResponse)
async def introduction(request: Request):
        # with open('static/information.html') as fh:
        #     data = fh.read()
        return FileResponse("static/information.html")#HTMLResponse(content=data, media_type="html")

@app.get("/planets")
def planet_list():
    return FileResponse("static/planets_list.html")

@app.get("/planets/{planet_name}")
def show_a_planet_info(planet_name: str):
      
        planets = {
             "sun" : {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"
             } ,
             "mercury" :{
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                    
             } ,
             "venus" : {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                    
             } ,
             "earth" : {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                   
             } ,
             "mars" : {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                    
             } , 
             "jupiter" : {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                   
             },
             "saturn": {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                 
             },
             "uranus": {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                   
             },
             "neptune": {
                    "radius" : 1 , 
                    "Distance_from_Sun" : 0 ,
                    "Distance_from_Earth" : 2 ,
                    "information" : "info"                   
             }
        }

        return planets[planet_name]


@app.get("/planets/{planet_name}/image")
def image_of_a_planet(planet_name : str):
       
    return FileResponse(f"planets_images/{planet_name}.jpg")
