import streamlit as st

st.title("Welcome!!!")
st.header("This is the ultimately basic chatbot made by VINEET⚡ using Streamlit in Python.")
st.subheader("Source code:")
st.code('''
    # Main chatbot code
    import streamlit as st
    from time import sleep
    from groq import Groq

    client = Groq(api_key = Can't show personal info here)
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

    # History page code
    import streamlit as st

    st.header("Peek into your chat history...")
    if "chat_history" in st.session_state:
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
''')

st.markdown('''
    NOTE: In future I might add some additional features like file uploading, voice search, etc.
''')

with st.sidebar:
    st.title("Socials")
    st.page_link(label = "Instagram", page = "https://www.instagram.com/_k.vineettt?igsh=aXNpNzJpd2Ewb280", icon = "🔗")
