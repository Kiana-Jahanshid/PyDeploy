import streamlit as st

st.title("first streamlit app")
st.write("hellow world")

with st.sidebar :
    color = st.color_picker("pick a color")

    agree = st.checkbox("select")
    vl = st.slider("select a range : " , 0.0 , 300.0 , (25.0 , 100.0))
    link = st.radio("pick one" , ["option 1" , "option_2"])




col1 , col2 = st.columns(2)



with col1 :

    btn = st.button("click on me 😊")

    if btn : 
        st.write("hi")
    else :
        st.write("by")



    st.text_input("firstname")
    st.text_input("lastname")


print("hi ") # با هر بار کلیک روی دکمه ، کد دوباره اجرا میشه 

with col2 :
    weight  =  st.number_input("Enter your weight (kg) : ")
    height = st.number_input("Enter your height (cm) : ")



    button_calculate_BMI = st.button("Calculate BMI")

    if button_calculate_BMI :
        bmi = weight / ((height / 100)** 2)
        st.write(bmi)

        if bmi < 18.5 :
            st.success("slim")
        elif 18.5 < bmi < 25 :
            st.info("normal")
        elif 28 > bmi > 25 :
            st.warning("fat")
        elif bmi > 28 :
            st.error("over weight")


    else :
        st.write("enter your info then press the button")





st.title("new line is here out of columns ")


