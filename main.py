import streamlit as st
from google import genai

# Mobile UI Page Settings
st.set_page_config(page_title="AI NANBAN", page_icon="🤖")

st.title("🤖 AI NANBAN")
st.write("Online 🟢")

# Safe API Key Implementation Block
API_KEY = "AQ.Ab8RN6LYqLe30ycVp9TEdaPfs7s8vD2A_f8lImZRJjWe6qkBsw"

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

    # AI Response Compilation
    try:
        client = genai.Client(api_key=API_KEY.strip())
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
        )
        ai_response = response.text
    except Exception as ex:
        ai_response = f"Error: {str(ex)}"

    with st.chat_message("assistant"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
