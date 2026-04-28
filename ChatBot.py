import streamlit as st
from groq import Groq

client = Groq(api_key = "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")
prompt = st.chat_input(placeholder = "What's in your mind...?")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if prompt == None:
    st.header("Ask anything you want...", text_alignment = 'center')
else:
    st.session_state.chat_history.append({"role":"user", "content":prompt})

    with st.chat_message(name = "Human"):
        st.write(prompt)

    with st.chat_message(name = "AI"):
        reply = ask_ai(prompt)
        st.session_state.chat_history.append({"role":"AI", "content":reply})
        st.write(reply)

with st.sidebar:
    st.title("Socials")
    st.page_link(label = "Instagram", page = "https://www.instagram.com/_k.vineettt?igsh=aXNpNzJpd2Ewb280", icon = "🔗")
