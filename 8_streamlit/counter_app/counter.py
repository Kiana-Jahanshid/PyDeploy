import streamlit as st

st.set_page_config("Counter App" , "🎰")

purple_btn_colour = """
                        <style>
                            div.stButton > button:first-child {background-color: #00FA9A ;primaryColor:"#00FA9A" ;border-color:"#00FA9A" ; color:#00FA9A ;height:4em;width:4em; border-radius:31px 31px 31px 31px;}
                        </style>
                    """

st.markdown(purple_btn_colour, unsafe_allow_html=True)
st.markdown("<style> div[class^='css-1vbkxwb'] > p { font-size: 1.5rem; } </style> ", unsafe_allow_html=True)

c1, c2, c3 = st.columns([11, 25 , 2])
with c1:
    st.write("")
with c2 :
    st.title('🎰 Counter App')
with c3 :
    st.write("")

st.write("")
" "
st.write("")
" "
st.write("")
" "
st.write("")

col0 , col1, col2, col3   = st.columns([2.3 ,3.5 ,3 ,3])


#Check if 'count_number' already exists in session_state
#If not, then initialize it
if 'counter' not in st.session_state:
    st.session_state.counter = 0


with col1:
    minus_btn = st.button("➖")
    if minus_btn :
        st.session_state.counter -= 1

with col3:
    plus_btn = st.button('➕' )
    if plus_btn:
        st.session_state.counter += 1

with col2:
    st.header(st.session_state.counter )
    
