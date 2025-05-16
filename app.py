import streamlit as st
from chatbot import respond

st.set_page_config(page_title="📝 TaskBot", layout="centered")

st.title("💬 TaskBot - Your Chat-Based To-Do List")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("task_input"):
    user_input = st.text_input("Type your task or command:")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        response = respond(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("TaskBot", response))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
