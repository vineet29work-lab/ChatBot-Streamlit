import streamlit as st

st.header("Peek into your chat history...")
if "chat_history" in st.session_state:
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

with st.sidebar:
    st.title("Socials")
    st.page_link(label = "Instagram", page = "https://www.instagram.com/_k.vineettt?igsh=aXNpNzJpd2Ewb280", icon = "🔗")
