import streamlit as st 
from sqlmodel import Field , Session , SQLModel , create_engine , select, Relationship 
from typing import Optional
from sqlalchemy.orm import sessionmaker


class UserAuth(SQLModel , table=True): # table= True means : create table from this class
    # if a table is existed , there is no need to create it again 
    __table_args__ = {"extend_existing" : True}
    
    id : Optional[int] = Field(default=None , primary_key=True)
    name : str
    username : str
    email : str 
    password : str

class Id():
    temp_id = 0

@st.cache_resource
def connect_db():
    engine = create_engine(url= "postgresql://root:iiHoGm4235pme3TKHs2tSBGh@ai-assistant:5432/postgres" , echo=True)#"sqlite:///auth_database.db"
    SQLModel.metadata.create_all(engine)
    return engine

engine = connect_db()



col1 , col2 = st.columns(2)
with col1 :
    if "users" not in st.session_state :
        st.session_state.users = []

    st.title("signup")

    with st.form("signup form"):
        user_name = st.text_input(label="Name" , placeholder=" Enter your name ... ")
        user_username = st.text_input(label="Username" , placeholder="Enter a Username ....")
        user_email = st.text_input(label="Email" , placeholder="Enter your Email ...")
        user_password = st.text_input(label="Password" , placeholder="Enter a password")

        user_info = UserAuth(name=user_name , username=user_username , email=user_email , password=user_password)    

        submitted = st.form_submit_button("Submit")
        


    if submitted :
        
        with Session(engine) as session :
            check_username_existance = select(UserAuth).where(UserAuth.username == user_username)
            res = session.exec(check_username_existance)
            res = res.first()
            print(res)

            correct_format = user_email[-10:] 
            print(correct_format)

            if (res is None) and (correct_format in ("@gmail.com" ,"@yahoo.com")):
                session.add(user_info)
                session.commit()
                st.success("signup completeted successfully ")

                current_user = select(UserAuth).where(UserAuth.username == user_username)
                res = session.exec(current_user)
                res = res.first()
                print("res : " , res)
                print("user_id : " , res.id)
                Id.temp_id = res.id

            elif res is not None : 
                st.error(body="❌ This USERNAME is already taken , choose another one . ")

            elif correct_format not in ( "@gmail.com" , "@yahoo.com" ) :
                st.error(body="your EMAIL format is wrong , email should be finished with '@gmail.com' or '@yahoo.com' ")
            


with col2 :
    st.title("login")

    with st.form("login form"):
        login_username = st.text_input(label="UserName" , placeholder="Enter your username ...")
        login_pass = st.text_input(label="Password" , placeholder="Enter your password ...")

        submit = st.form_submit_button("Submit")


    if submit :
        with Session(engine) as session :
            check_username = select(UserAuth).where(UserAuth.username == login_username)
            check_username = session.exec(check_username)
            check_username = check_username.first() # entire row


            if check_username is None :
                database_pass = "temp"
            if (check_username is None) and (login_pass != database_pass)  :
                st.error(body="username or password is wrong . Try again ... ")

            # go to chat page 
            else :
                Id.temp_id = check_username.id
                print("user_id2 " , Id.temp_id)
                st.success("You loged in successfully")
                st.empty()
                st.switch_page("pages/chatbot.py")



















# if submitted :
#     with Session(engine) as session :

#         if select(UserAuth).where(UserAuth.username == user_username) is not None:
#             st.error(body="❌ This username is already taken , choose another one . ")
#         else :
#             session.add(user_info)
#             session.commit()
#             st.success("signup completeted successfully ")

#             # Perform query.
#         #with Session(engine) as session :
#             current_user = select(UserAuth).where(UserAuth.username == user_username)
#             res = session.exec(current_user)
#             res = res.first()
#             print("user_id" , res.id)   







# Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")


# # Creating a new user registration widget
# try:
#     (user_name , user_username , user_email , password) = 
#     if user_email:
#         st.success('User registered successfully')
# except RegisterError as e:
#     st.error(e)



# Creating a login widget
# try:
#     authenticator.login()
# except LoginError as e:
#     st.error(e)

# if st.session_state["authentication_status"]:
#     authenticator.logout()
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')


# Creating a password reset widget
# if st.session_state["authentication_status"]:
#     try:
#         if authenticator.reset_password(st.session_state["username"]):
#             st.success('Password modified successfully')
#     except ResetError as e:
#         st.error(e)
#     except CredentialsError as e:
#         st.error(e)




# Creating a forgot password widget
# try:
#     (username_of_forgotten_password,
#         email_of_forgotten_password,
#         new_random_password) = authenticator.forgot_password()
#     if username_of_forgotten_password:
#         st.success('New password sent securely')
#         # Random password to be transferred to the user securely
#     elif not username_of_forgotten_password:
#         st.error('Username not found')
# except ForgotError as e:
#     st.error(e)



# # Creating a forgot username widget
# try:
#     (username_of_forgotten_username,
#         email_of_forgotten_username) = authenticator.forgot_username()
#     if username_of_forgotten_username:
#         st.success('Username sent securely')
#         # Username to be transferred to the user securely
#     elif not username_of_forgotten_username:
#         st.error('Email not found')
# except ForgotError as e:
#     st.error(e)






# Saving config file



#print(st.session_state["username"])

