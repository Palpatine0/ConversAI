import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def init():
    load_dotenv()

    st.set_page_config(
        page_title = "Converse AI",
        page_icon = "🤯",
        layout = "wide",
        initial_sidebar_state = "expanded",
    )


def main():
    init()

    st.header("Your own ChatGPT")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key = "user_input")


if __name__ == "__main__":
    main()
