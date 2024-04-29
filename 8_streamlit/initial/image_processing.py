import cv2
import numpy as np
from PIL import Image
import streamlit as st



st.title("Image Blurring App")

with st.sidebar:
    blur_value = st.slider("how much do you want to blur image ? select a value :" ,
                            min_value= 1 , max_value= 150 , value= 5 , step=2 ) # odd value for blur mask
    

file = st.file_uploader("upload an image :  " , type=["jpg" , "png" , "jpeg"])


if file is not None :
    st.success("file loaded successfully")
    

    image = Image.open(file)
    init_image = st.image(file)

    image = np.array(image)

    image = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)


    
    result = cv2.blur(image , (blur_value , blur_value ))

    res = cv2.cvtColor(result , cv2.COLOR_BGR2RGB)
    res = Image.fromarray(res)
    st.image(res) # imshow()


else : 

    st.info("nothing is loaded yet !")

















