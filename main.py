import streamlit as st

st.set_page_config(
    page_title = "Converse AI",
    page_icon = "🤯",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

st.header("Your own ChatGPT")

with st.sidebar:
    user_input = st.text_input("Your message: ", key = "user_input")
