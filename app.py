# app.py

from dotenv import load_dotenv  # type: ignore
import os
import google.generativeai as genai  # type: ignore
import streamlit as st  # Import Streamlit

# Load environment variables
load_dotenv()

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate response using the Gemini model
def text_to_text_chatbot(question):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

def run_chatbot_app():
    st.title("FitLife Chatbot:")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input from the user
    if prompt := st.chat_input("What is your question?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response from Google Gemini
        response_text = text_to_text_chatbot(prompt)  # Call the function to get the response

        # Append the assistant's response to the messages
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        with st.chat_message("assistant"):
            st.markdown(response_text)

if __name__ == "__main__":
    run_chatbot_app()