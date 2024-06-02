import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

st.set_page_config(
    page_title = "Converse AI",
    page_icon = "🤯",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

st.header("Your own ChatGPT")

message("Hello! I'm ChatGPT. How can I help you today?")
message("Yooo! I'm gooooood!", is_user = True)

with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")
