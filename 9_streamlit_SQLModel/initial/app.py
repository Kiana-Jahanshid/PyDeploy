import streamlit as st 
from streamlit_pdf_viewer import pdf_viewer

# we are using 2 unofficial streamlit component 


# load pdf with ( streamlit pdf viewer)
# 1_ pip install streamlit-pdf-viewer
# 2_ streamlit run app.py

#pdf_viewer(input="Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.pdf")

#import streamlit_authenticator
# stremlit authenticator : (for login , create account , ...)
# pip install streamlit-authenticator 

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (CredentialsError,
                                                          ForgotError,
                                                          LoginError,
                                                          RegisterError,
                                                          ResetError,
                                                          UpdateError) 



# Loading config file for saving user informations
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Creating a login widget
try:
    authenticator.login()
except LoginError as e:
    st.error(e)

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    pdf_viewer(input="Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.pdf")

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')


# Creating a password reset widget
if st.session_state["authentication_status"]:
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except ResetError as e:
        st.error(e)
    except CredentialsError as e:
        st.error(e)


# # Creating a new user registration widget
try:
    (email_of_registered_user,
        username_of_registered_user,
        name_of_registered_user) = authenticator.register_user(pre_authorization=False)
    if email_of_registered_user:
        st.success('User registered successfully')
except RegisterError as e:
    st.error(e)

# Creating a forgot password widget
try:
    (username_of_forgotten_password,
        email_of_forgotten_password,
        new_random_password) = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password sent securely')
        # Random password to be transferred to the user securely
    elif not username_of_forgotten_password:
        st.error('Username not found')
except ForgotError as e:
    st.error(e)

user = st.session_state


# # Creating a forgot username widget
try:
    (username_of_forgotten_username,
        email_of_forgotten_username) = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username sent securely')
        # Username to be transferred to the user securely
    elif not username_of_forgotten_username:
        st.error('Email not found')
except ForgotError as e:
    st.error(e)

# # Creating an update user details widget
if st.session_state["authentication_status"]:
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except UpdateError as e:
        st.error(e)

# Saving config file
with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)




print(st.session_state["username"])

