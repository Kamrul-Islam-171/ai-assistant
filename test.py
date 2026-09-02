import streamlit as st

from chatbot import get_response


st.set_page_config(
    page_title="LangChain AI Chatbot",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 LangChain AI Chatbot")

st.caption(
    "RunnableBranch + RunnableParallel + Pydantic Structured Output"
)


# --------------------------------------------------
# Chat History
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# User Input
# --------------------------------------------------

question = st.chat_input(
    "Ask me anything..."
)


if question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(question)

        st.markdown(response.answer)

        with st.expander("Structured Output"):

            st.write(
                {
                    "answer": response.answer,
                    "summary": response.summary,
                    "category": response.category,
                    "confidence": response.confidence,
                    "keywords": response.keywords,
                }
            )

    # Store assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.answer,
        }
    )