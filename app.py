# app.py

from dotenv import load_dotenv  # type: ignore
import os
import google.generativeai as genai  # type: ignore

# Load environment variables
load_dotenv()

# Configure API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate response using the Gemini model
def text_to_text_chatbot(question):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

# Optional: Only run Streamlit app if this script is executed directly
if __name__ == '__main__':
    import streamlit as st  # Only import Streamlit when running standalone

    st.set_page_config(page_title="Q&A Demo")

    st.header("Gemini Application")

    user_input = st.text_input("Input: ", key="input")

    submit = st.button("Ask the question")

    # If the button is clicked
    if submit:
        if user_input:
            response = text_to_text_chatbot(user_input)  # Call the function
            st.subheader("The Response is")
            st.write(response)
        else:
            st.warning("Please enter a question.")