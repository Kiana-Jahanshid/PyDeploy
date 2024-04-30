import streamlit as st
import pandas as pd
from PIL import Image
import os

st.set_page_config("Data Science App" , "📊")
st.title("🎭🎬 Netflix Movies and TV Shows")
st.subheader("Exploring the Depths of Netflix: A Comprehensive Dataset of Movies and TV Shows")

st.write(" ")
st.write(" ")

dir_name = os.path.abspath(os.path.dirname(__file__))
location = os.path.join(dir_name, 'netflix_titles.csv')

df = pd.read_csv(location)
df.to_csv().encode('utf-8')
df = df[df.columns[:12]]
df = df.dropna()
df = df.drop(columns=["show_id"])
st.dataframe(df )


col1 , col2  = st.columns([6,6])
with col1:
    st.subheader('Distribution of Content Across Countries on Netflix')
    country_counts = df['country'].value_counts().head(15).sort_values(ascending=False) # Displaying the top 15 countries
    st.bar_chart(country_counts , width= 110 , color="#33FF57")
    

with col2:
    st.subheader('Distribution of Content Types on Netflix')
    content_type_counts = df['type'].value_counts()
    #fig = plt.figure(figsize=(5, 4))
    #content_type_counts.plot(kind='bar', color=['blue', 'red'] )
    #st.pyplot(content_type_counts)
    st.bar_chart(content_type_counts , width= 110 , color="#3CFEDA" )



with st.sidebar:
    st.subheader("About this App : ")
    st.write("The Netflix Titles dataset is a comprehensive compilation of movies and TV shows available on Netflix, covering various aspects such as the title type, director, cast, country of production, release year, rating, duration, genres, and a brief description.")
    st.write(" This dataset is instrumental for analyzing trends in Netflix content, understanding genre popularity, and examining the distribution of content across different regions and time periods.")


    image = Image.open("netflix.jpg")

st.sidebar.image(image)


#st.sidebar()