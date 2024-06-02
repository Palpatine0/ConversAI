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

    if "messages" not in st.session_state:
        # Create a list to hold the messages
        st.session_state.messages = [
            # Starting with a system message to set the context
            SystemMessage(content = "You are a helpful assistant."),
        ]

    st.header("Your own ChatGPT")

    with st.sidebar:
        user_input = st.text_input("Your message: ", key = "user_input")
        if user_input:
            # Append the user's message to the conversation history
            st.session_state.messages.append(HumanMessage(content = user_input))
            with st.spinner("Thinking..."):
                # Get the model's response based on the conversation history
                response = llm(st.session_state.messages)
            # Append the AI's response to the conversation history
            st.session_state.messages.append(AIMessage(content = response.content))

    # Retrieve the messages from the session state and iterate over the messages starting from the second one to skip the sys msg
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user = True, key = str(i) + '_user')
        else:
            message(msg.content, is_user = False, key = str(i) + '_ai')


if __name__ == "__main__":
    main()
