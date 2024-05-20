import streamlit as st
from sqlmodel import Field , Session , SQLModel , create_engine , select
from models import User , Message # these 2 class will create 2 table
import authenticator 
import json
import requests
import dotenv
import os


#dotenv = dotenv.load_dotenv()
#API_KEY = os.getenv("APIkey")



# در هربار اجرای استریملیت این مدل ها هم ایمپورت میشن 
# و هی تیبل اش میخواد ساخته بشه 
# solution : use <<<<< __table_args__ >>>>> in models file


# <<< Problem >>> :
# streamlit re-executes our script with each user interaction .
# in streamlit , in each sending message , this connection to database will be run again
# and database will be open and close every time for each message
# its time consuming

# streamlit solution : (https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)
# use st.cache_resource DECORATOR 
# when we want to use database connection in streamlit
# and only reload in first step of loading browser 

# only in first step , connection to database established
# and CACHE this connection from second step 
# and this decorator will not run again after first step
# از دفعه دوم ، اتصال به دیتابیس کش میشه 
@st.cache_resource
def connecting_to_db():
    # CONNECTING TO DATABASE
    # this database will save chats between user and ai-assistant
    engine = create_engine(url="postgresql://root:aD81gNCc4Z2V5RkXRfP1Uft4@user-assistant-chats:5432/postgres")#"sqlite:///database.db"
    SQLModel.metadata.create_all(engine)
    return engine

engine = connecting_to_db()

# in session_state variables will remain in each run


def process(user_text_message):

    ai_text_message = ai(user_text_message=user_text_message)

    # frontend 
    st.session_state.messages.append({'type' : 'user' , 'text' : user_text_message})
    st.session_state.messages.append({'type' :'ai' , 'text' : ai_text_message})

    # backend (using session.add)
    # به ازای هر پیام جدید ،‌ اطلاعات توی دیتابیس هم اد بشه 
    # id is automatically being set
    user_message = Message(text= user_text_message , type="user" , user_id=authenticator.Id.temp_id) # این یک باید عوض بشه using streamlit_authenticator and app.py
    ai_message = Message(text= ai_text_message , type= "ai" , user_id=authenticator.Id.temp_id)

    with Session(engine) as session :
        session.add(user_message)
        session.add(ai_message)
        session.commit()

    return ai_text_message


 
def ai(user_text_message):

    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODc2NTMyMTUtZmE4ZC00YmVjLWFkNGQtMTU3YzM5ZmRmZTBmIiwidHlwZSI6ImFwaV90b2tlbiJ9.QenqIwNKpzfLv5VJWIFYU6d_sSvsOYEIrbvXd64UJns"}

    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": user_text_message,
        "chatbot_global_action": "Act as an assistant",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": "emvista"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])
    response = result['openai']['generated_text']
    return response




if "messages" not in st.session_state :
    st.session_state.messages = []


for message in st.session_state.messages :
    with st.chat_message(message["type"]):
        st.write(message["text"])

if user_text_message := st.chat_input("send new message") : 

    ai_text_message =  process(user_text_message)
    with st.chat_message("user"):
        st.write(user_text_message)

    with st.chat_message("ai"):
        st.write(ai_text_message)







# how to run :
# streamlit run chatbot.py