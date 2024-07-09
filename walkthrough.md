# Converse AI

## Objective

In this project, we'll build a ChatGPT clone with a graphical user interface using Python. We'll use Streamlit for the
interface and LangChain to handle communication with language models. This straightforward and highly useful project
will result in a fully functional chatbot that can remember previous interactions. This is ideal for creating
specialized chatbots for PDFs or CSV files. Let's get started and bring this innovative chatbot to life!

## Prerequisites

Before starting, ensure you have the following installed on your system:

- Python 3.11 or higher
- pip (Python package installer)
- Git (optional)

### Step 1: Initial Setup

#### 1. Environment Setup

To start, we need to manage sensitive information such as API keys securely. Using a `.env` file is a standard practice
for this purpose.

1. **Create a `.env` file:**
    - This file will store your OpenAI API key. Ensure it is included in your `.gitignore` file to prevent it from being
      committed to your repository.

   Example `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install required packages:**

   ```bash
   pip install langchain openai streamlit python-dotenv
   ```

   ```bash
   pip install langchain_community
   ```

### Step 2: Initialize Streamlit Project

In this step, we'll set up a basic Streamlit project to create the graphical user interface for our ChatGPT clone. This
will involve configuring the page settings and adding a header to the main page.

#### 1. Create `main.py`

Create a file named `main.py` in the root directory of your project. This will be the main entry point for our Streamlit
application.

**File**: `main.py`

**Code for `main.py`**:

```python
import streamlit as st

st.set_page_config(
    page_title = "Converse AI",
    page_icon = "🤯",
    layout = "wide",
    initial_sidebar_state = "expanded",
)

st.header("Your own ChatGPT")
```

##### Explanation of the Code

1. **Import Streamlit**:
    - The `streamlit` module is imported to use its functions for creating the user interface.

2. **Set Page Configuration**:
    - `st.set_page_config` is used to configure the page settings such as the title, icon, layout, and initial sidebar
      state.
        - `page_title`: Sets the title of the webpage to "Converse AI".
        - `page_icon`: Sets the icon of the webpage to an emoji (🤯).
        - `layout`: Sets the layout of the page to "wide" to utilize the full width of the browser window.
        - `initial_sidebar_state`: Sets the initial state of the sidebar to "expanded".

3. **Add a Header**:
    - `st.header` is used to add a header to the main page with the text "Your own ChatGPT".

#### 2. Run the Streamlit Application

To test the setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should see a
webpage with the configured title, icon, and header.

By completing this step, you've successfully initialized a basic Streamlit project for building your ChatGPT clone. In
the next steps, we will integrate LangChain to handle communication with language models and add more functionality to
the user interface.

### Step 3: Add User Input Text Box in Sidebar

In this step, we will add a text input field in the sidebar for users to enter their messages. This will allow users to
interact with our ChatGPT clone.

#### 1. Update `main.py`

Modify the `main.py` file to include a text input field in the sidebar.

**Updated Code for `main.py`**:

```python
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
```

##### Explanation of the Code

1. **Add a Text Input Field**:
    - `with st.sidebar:` is used to specify that the following elements should be placed in the sidebar.
    - `user_input = st.text_input("Your message: ", key="user_input")` adds a text input field to the sidebar.
        - `"Your message: "`: This is the label for the text input field.
        - `key="user_input"`: A unique key for the input field to manage its state.

#### 2. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should see the
sidebar with a text input field labeled "Your message:" where users can enter their messages.

<img src="https://i.imghippo.com/files/cpHfA1717325100.png" alt="" border="0">

By completing this step, you've added the capability for users to input their messages in the sidebar. In the next
steps, we will process these messages using LangChain to communicate with the language model and generate responses.

### Step 4: Add Chat Messages

In this step, we will enhance the application by displaying chat messages on the main page. We will use
the `streamlit_chat` library to handle chat messages.

#### 1. Install `streamlit-chat`

First, install the `streamlit-chat` package using the following command:

```bash
pip install streamlit-chat
```

#### 2. Update `main.py`

Modify the `main.py` file to include chat messages.

**Updated Code for `main.py`**:

```python
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
```

##### Explanation of the Code

1. **Import `streamlit_chat` and `dotenv`**:
    - `from streamlit_chat import message`: Import the `message` function from `streamlit_chat` to handle chat messages.
    - `from dotenv import load_dotenv`: Import `load_dotenv` to load environment variables from the `.env` file.

2. **Add Initial Chat Messages**:
    - `message("Hello! I'm ChatGPT. How can I help you today?")`: Display a message from ChatGPT.
    - `message("Yooo! I'm gooooood!", is_user=True)`: Display a user message. The `is_user=True` parameter indicates
      that the message is from the user.

#### 3. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should see the
initial chat messages displayed on the main page.

<img src="https://i.imghippo.com/files/f0jTf1717325158.jpg" alt="" border="0">

By completing this step, you've added the capability to display chat messages on the main page. In the next steps, we
will integrate LangChain to process user inputs and generate responses dynamically.

### Step 5: Refactor Code and Add LangChain Integration

In this step, we'll refactor the code to improve organization and readability. Additionally, we'll integrate LangChain
to handle chat interactions dynamically. Note that currently, the chatbot does not have any memory settings, so each
interaction is treated independently.

#### 1. Update `main.py`

Modify the `main.py` file to include LangChain integration and refactor the code structure.

**Updated Code for `main.py`**:

```python
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

    # Add a button to submit the user's message
    if st.sidebar.button("Send"):
        # Initialize LangChain's ChatOpenAI model
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        chat_model = ChatOpenAI(api_key = openai_api_key)

        # Create a system message to instruct the AI
        system_message = SystemMessage(content = "You are a helpful assistant.")

        # Create a human message from the user's input
        human_message = HumanMessage(content = user_input)

        # Send messages to the AI and get a response
        ai_response = chat_model([system_message, human_message])

        # Display the chat messages
        message("Hello! I'm ChatGPT. How can I help you today?")
        message(user_input, is_user = True)
        message(ai_response.content)


if __name__ == "__main__":
    main()
```

##### Explanation of the Code

1. **Import LangChain Components**:
    - `from langchain.chat_models import ChatOpenAI`: Import the `ChatOpenAI` model from LangChain.
    - `from langchain.schema import SystemMessage, HumanMessage, AIMessage`: Import message types from LangChain.

2. **Initialize Function**:
    - `init()`: Function to load environment variables and set Streamlit page configuration.

3. **Main Function**:
    - `main()`: Function to initialize the environment, display the header, and handle user input.
    - Added a button in the sidebar to submit the user's message.
    - Initialized LangChain's `ChatOpenAI` model with the API key from environment variables.
    - Created a system message to instruct the AI.
    - Created a human message from the user's input.
    - Sent messages to the AI model and got a response.
    - Displayed the chat messages using `streamlit_chat`.

#### 2. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should now be
able to enter a message in the sidebar, click "Send," and see the AI response displayed on the main page.

<img src="https://i.imghippo.com/files/TNDdl1717329147.jpg" alt="" border="0">
<img src="https://i.imghippo.com/files/ffmGy1717329191.jpg" alt="" border="0">


As the responses show, currently, the chatbot does not have any memory settings, meaning it does not retain context
between interactions. Each user message is treated as an independent query.

By completing this step, you've refactored the code for better organization and readability and integrated LangChain to
handle chat interactions dynamically. In the next steps, we will enhance the chatbot's functionality and improve the
user experience.

### Step 6: Integrate ChatOpenAI for Dynamic Chat Responses

In this step, we will enhance the chatbot by integrating LangChain's `ChatOpenAI` for generating dynamic responses. This
will enable the chatbot to handle ongoing conversations and provide contextually relevant replies based on user input.

#### 1. Update `main.py`

Modify the `main.py` file to include message handling and conversation history for generating AI responses dynamically.

**Updated Code for `main.py`**:

```python
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
```

##### Explanation of the Code

1. **Initialize ChatOpenAI**:
    - `llm = ChatOpenAI(temperature=1)`: Initialize the ChatOpenAI model with a temperature setting for generating
      responses.

2. **Conversation History**:
    - `messages`: Create a list to hold the messages, starting with a system message to set the context for the AI.

3. **Message Handling**:
    - Display the user message in the chat interface using `message(user_input, is_user=True)`.
    - Append the user's message to the conversation history using `messages.append(HumanMessage(content=user_input))`.
    - Get the model's response based on the conversation history using `response = llm(messages)`.
    - Display the model's response in the chat interface using `message(response.content, is_user=False)`.

#### 2. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should now be
able to enter a message in the sidebar, click "Send," and see the AI response displayed on the main page, with the
chatbot remembering the context of the conversation.

<img src="https://i.imghippo.com/files/QVpvP1717330827.png" alt="" border="0">
<img src="https://i.imghippo.com/files/Bexnb1717330906.png" alt="" border="0">

By completing this step, you've integrated LangChain's `ChatOpenAI` for dynamic chat responses and implemented
conversation history to provide contextually relevant replies based on user input. This makes the chatbot more
interactive and capable of handling ongoing conversations.

### Step 7: Persist Chat Messages Using Streamlit Session State

In this step, we will enhance the chatbot by ensuring that chat messages are persisted across interactions using
Streamlit's session state. This will allow the conversation history to be maintained as users continue to interact with
the chatbot.

#### 1. Update `main.py`

Modify the `main.py` file to use Streamlit's session state for storing and persisting conversation history.

**Updated Code for `main.py`**:

```python
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
        # Display the user message in the chat interface
        message(user_input, is_user = True)
        # Append the user's message to the conversation history
        st.session_state.messages.append(HumanMessage(content = user_input))
        # Get the model's response based on the conversation history
        response = llm(st.session_state.messages)
        # Display the model's response in the chat interface
        message(response.content, is_user = False)


if __name__ == "__main__":
    main()
```

##### Explanation of the Code

1. **Check for Session State**:
    - `if "messages" not in st.session_state`: Check if the `messages` key is in the session state.
    - If not, initialize the session state with a list containing a system message to set the context.

2. **Persist Messages in Session State**:
    - Append user and AI messages to `st.session_state.messages` to maintain the conversation history across
      interactions.

3. **Use Session State Messages**:
    - Use `st.session_state.messages` to pass the conversation history to the language model for generating responses.

#### 2. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should now be
able to enter messages in the sidebar, and the chatbot will maintain the conversation history across interactions.

<img src="https://i.imghippo.com/files/FSxv01717333794.jpg" alt="" border="0">

By completing this step, you've ensured that chat messages are persisted across interactions using Streamlit's session
state. This enhances the chatbot's usability by maintaining the context of the conversation, making it more interactive
and user-friendly.

### Step 8: Persist and Display Chat History

In this step, we will improve the chatbot by persisting and displaying the entire chat history. This will include
handling user input within a sidebar form, appending AI responses to the conversation history, and displaying the chat
history in the main interface.

#### 1. Update `main.py`

Modify the `main.py` file to handle user input within a form, append AI responses, and display the chat history.

**Updated Code for `main.py`**:

```python
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

    # Retrieve the messages from the session state and iterate over the messages starting from the second one to skip the system message
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user = True, key = str(i) + '_user')
        else:
            message(msg.content, is_user = False, key = str(i) + '_ai')


if __name__ == "__main__":
    main()
```

##### Explanation of the Code

1. **Handle User Input within the Sidebar**:
    - The user input is now handled within the sidebar form using `st.text_input`.

2. **Append AI Responses to Conversation History**:
    - AI responses are appended to the conversation history using `st.session_state.messages`.

3. **Display Chat History**:
    - The chat history is retrieved from the session state and displayed in the main interface. Messages are alternated
      between user and AI messages.

4. **Use a Spinner While Processing**:
    - A spinner (`st.spinner`) is used to indicate that the AI is processing the response.

#### 2. Run the Streamlit Application

To test the updated setup, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This command will start the Streamlit server and open the application in your default web browser. You should now be
able to enter messages in the sidebar, and the chatbot will maintain and display the conversation history across
interactions.

By completing this step, you've enhanced the chatbot by ensuring that the entire chat history is persisted and
displayed. This makes the chatbot more interactive and user-friendly by providing context for the conversation.