import os
from typing import Union 
from fastapi import FastAPI , HTTPException , status , Response , Request 
from fastapi.responses import HTMLResponse , FileResponse , StreamingResponse
import cv2
import numpy as np
import io
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static" ))

@app.get("/" , response_class=HTMLResponse)
async def introduction(request: Request):
       # with open('static/information.html') as fh:
       #     data = fh.read()
       try :
              return FileResponse("static/information.html")#HTMLResponse(content=data, media_type="html")
       except :
              raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail="html not found")


@app.get("/planets")
def planet_list():
    try :
       return FileResponse("static/planets_list.html")
    except:
       raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail="html file not found")


@app.get("/planets/{planet_name}")
def show_a_planet_info(planet_name: str):
       try :   
              planets = {
                     "sun" : {
                            "radius" : " 696340 km" , 
                            "Distance_from_Sun" : " 0 km ",
                            "information" : "The Sun is the star at the heart of our solar system. Its gravity holds the solar system together, keeping everything , from the biggest planets to the smallest bits of debris in its orbit"
                     } ,
                     "mercury" :{
                            "radius" : "2439.7 km" , 
                            "Distance_from_Sun" : "50.236 million km",
                            "information" : "Mercury—the smallest planet in our solar system and nearest to the Sun—is only slightly larger than Earth's Moon. Its surface is covered in tens of thousands of impact craters. From the surface of Mercury, the Sun would appear more than three times as large as it does when viewed from Earth, and the sunlight would be as much as 11 times brighter."                    
                     } ,
                     "venus" : {
                            "radius" : "6051.8 km " , 
                            "Distance_from_Sun" : "108.92 million km",
                            "information" : "Venus is the second planet from the Sun, and the sixth largest planet. It's the hottest planet in our solar system. Venus is a cloud-swaddled planet named for a love goddess, and often called Earth's twin. But pull up a bit closer, and Venus turns hellish. Our nearest planetary neighbor, the second planet from the Sun, has a surface hot enough to melt lead. The atmosphere is so thick that, from the surface, the Sun is just a smear of light."                    
                     } ,
                     "earth" : {
                            "radius" : " 6371 km " , 
                            "Distance_from_Sun" : "149.3 million km" ,
                            "information" : "While Earth is only the fifth largest planet in the solar system, it is the only world in our solar system with liquid water on the surface. Just slightly larger than nearby Venus, Earth is the biggest of the four planets closest to the Sun, all of which are made of rock and metal."                   
                     } ,
                     "mars" : {
                            "radius" : "3389.5 km ", 
                            "Distance_from_Sun" : "209.73 million km" ,
                            "information" : "Mars is no place for the faint-hearted. It's dry, rocky, and bitter cold. The fourth planet from the Sun, Mars is one of Earth's two closest planetary neighbors (Venus is the other). Mars is one of the easiest planets to spot in the night sky , it looks like a bright red point of light."                    
                     } , 
                     "jupiter" : {
                            "radius" : "69911 km" , 
                            "Distance_from_Sun" : "748.19 million km" ,
                            "information" : "Jupiter is the fifth planet from the Sun and is, by far, the largest planet in the solar system , more than twice as massive as all the other planets combined.Jupiter's stripes and swirls are actually cold, windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium. Jupiter’s iconic Great Red Spot is a giant storm bigger than Earth that has raged for hundreds of years.Jupiter is named for the king of the ancient Roman gods. "                
                     },
                     "saturn": {
                            "radius" : "58232 km ", 
                            "Distance_from_Sun" : "1.4518 billion km" ,
                            "information" : "Saturn is the sixth planet from the Sun and the second largest planet in our solar system. Adorned with a dazzling system of icy rings, Saturn is unique among the planets.It is not the only planet to have rings, but none are as spectacular or as complex as Saturn's. Like fellow gas giant Jupiter, Saturn is a massive ball made mostly of hydrogen and helium."                 
                     },
                     "uranus": {
                            "radius" : "25362 km" , 
                            "Distance_from_Sun" : "2.9309 billion km" ,
                            "information" : "Uranus is the seventh planet from the Sun, and it's the third largest planet in our solar system , about four times wider than Earth. The diameter at its equator is 31,763 miles (51,120 kilometers).Uranus is a very cold and windy planet. It is surrounded by faint rings, and more than two dozen small moons as it rotates at a nearly 90-degree angle from the plane of its orbit. This unique tilt makes Uranus appear to spin on its side.Uranus is blue-green in color due to large amounts of methane, which absorbs red light but allows blues to be reflected back into space."                   
                     },
                     "neptune": {
                            "radius" : "24,622 km" , 
                            "Distance_from_Sun" : "4.4722 billion km" ,
                            "information" : "Dark, cold and whipped by supersonic winds, giant Neptune is the eighth and most distant major planet orbiting our Sun. More than 30 times as far from the Sun as Earth, Neptune is not visible to the naked eye. In 2011, Neptune completed its first 165-year orbit since its discovery.The planet's rich blue color comes from methane in its atmosphere, which absorbs red wavelengths of light, but allows blue ones to be reflected back into space."                   
                     }
              }
              keys = []
              values = []
              for i in range(len(planets[planet_name])):
                     keys.append(list(planets[planet_name].keys())[i])
                     values.append(list(planets[planet_name].values())[i])
              a = {keys[0]: values[0] }
              b = {keys[1]: values[1] }
              c = {keys[2]: values[2] }
              json_str = '\n'.join([json.dumps(a, default=str), json.dumps(b, default=str), json.dumps(c, default=str)])
              json_str = json_str.replace("{", "")
              json_str = json_str.replace("}", "")
              return Response(json_str, media_type='application/json') 
       except :
              raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail="bad request")

         

@app.get("/planets/{planet_name}/image")
def image_of_a_planet(planet_name : str):
    try :   
       return FileResponse(f"planets_images/{planet_name}.jpg")
    except :
       raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail="Image not found")

