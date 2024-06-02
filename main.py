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

    llm = ChatOpenAI(temperature = 1)

    # Create a list to hold the messages
    messages = [
        # Starting with a system message to set the context
        SystemMessage(content = "You are a helpful assistant."),
    ]

    st.header("Your own ChatGPT")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key = "user_input")

    if user_input:
        # Display the user message in the chat interface
        message(user_input, is_user = True)
        # Append the user's message to the conversation history
        messages.append(HumanMessage(content = user_input))
        # Get the model's response based on the conversation history
        response = llm(messages)
        # Display the model's response in the chat interface
        message(response.content, is_user = False)


if __name__ == "__main__":
    main()
