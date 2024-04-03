from typing import Union
from fastapi import FastAPI , Form , File , UploadFile , HTTPException
from fastapi.responses import StreamingResponse , FileResponse 
import io
import cv2
import numpy as np
import easyocr


app = FastAPI()


@app.post("/OCR/{language}")
async def optical_character_recognition(language:str="english" , input:UploadFile=Form(None)):

    if not input.content_type.startswith("image/"):
        raise HTTPException(status_code=415 , detail="file type error")
    
    else :

        init_image = await input.read()
        NumpyArray = np.frombuffer(buffer= init_image , dtype=np.uint8)
        decoded_image = cv2.imdecode(NumpyArray , cv2.IMREAD_UNCHANGED)
        
        reader_en = easyocr.Reader(lang_list=["en"])
        reader_fa = easyocr.Reader(lang_list=["fa"])
        textlist = ""
        en = ["english" , "English" ]
        fa = ["persian" ,"Persian" ,"farsi" ,"Farsi"]
        if language in en :
                text = reader_en.readtext(decoded_image)      
        elif language in fa:
                text = reader_fa.readtext(decoded_image)
        else :
             raise HTTPException(status_code=415 , detail="only english & persian(farsi) can be recognized")
         
        for i in range(len(text)):
            textlist = textlist +" "+ text[i][1]
        extracted_text = textlist

        return extracted_text 
