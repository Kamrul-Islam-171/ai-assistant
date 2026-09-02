import streamlit as st

from chatbot import get_response


st.set_page_config(
    page_title="AI Assistant",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Assistant")

if "chats" not in st.session_state:
    st.session_state.chats = {}
    
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = "chat_1"  


# Create First Chat If No Chat Exists
if not st.session_state.chats:

    st.session_state.chats["chat_1"] = {
        "title": "New Chat",
        "messages": [],
    }  
    

with st.sidebar :
    st.title("💬 Chat History")    
    
    if st.button(
        "➕ New Chat",
        use_container_width=True,
    ):

        chat_number = len(st.session_state.chats) + 1

        chat_id = f"chat_{chat_number}"

        st.session_state.chats[chat_id] = {
            "title": "New Chat",
            "messages": [],
        }

        st.session_state.current_chat_id = chat_id

        st.rerun()

    st.divider()
    
     # Display all previous chats
    for chat_id, chat in st.session_state.chats.items():

        title = chat["title"]

        if st.button(
            title,
            key=chat_id,
            use_container_width=True,
        ):

            st.session_state.current_chat_id = chat_id

            st.rerun()



current_chat = st.session_state.chats[
    st.session_state.current_chat_id
]

for message in current_chat["messages"]:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])   
        
        
question = st.chat_input(
    "Ask me anything..."
)
 
 
if question:

    current_chat["messages"].append(
        {
            "role": "user",
            "content": question,
        }
    )

    if current_chat["title"] == "New Chat":

        current_chat["title"] = question[:40]


    with st.chat_message("user"):

        st.markdown(question)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = get_response(question)


        # Display AI answer
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

    current_chat["messages"].append(
        {
            "role": "assistant",
            "content": response.answer,
        }
    )                 