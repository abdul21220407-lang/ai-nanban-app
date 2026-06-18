import streamlit as st
import google.generativeai as genai

# Mobile UI Page Settings
st.set_page_config(page_title="AI NANBAN", page_icon="🤖")

st.title("🤖 AI NANBAN")
st.write("Online 🟢")

# Safe API Key Implementation Block
API_KEY = "AQ.Ab8RN6LYqLe30ycVp9TEdaPfs7s8vD2A_f8lImZRJjWe6qkBsw"

# Configure the legacy library
genai.configure(api_key=API_KEY.strip())

# Chat History setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Chat Input execution
if user_prompt := st.chat_input("Type a message nanba..."):
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # AI Response Compilation using active legacy model
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(user_prompt)
        ai_response = response.text
    except Exception as ex:
        ai_response = f"Error: {str(ex)}"

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
