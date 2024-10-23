from dotenv import load_dotenv  # type: ignore
import os
from PIL import Image  # type: ignore
import google.generativeai as genai  # type: ignore

# Load environment variables
load_dotenv()

# Configure the API key for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to generate response using Gemini model for image-based input
def image_to_text_chatbot(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Handle case when input text is provided or not
    if input_text != "":
       response = model.generate_content([input_text, image])
    else:
       response = model.generate_content(image)
       
    return response.text

# Optional: Only run Streamlit code when script is executed directly
if __name__ == '__main__':
    import streamlit as st  # Import Streamlit only when running standalone

    st.set_page_config(page_title="Gemini Image Describer")

    st.header("Gemini Application")

    # Input for text prompt (optional)
    input_text = st.text_input("Input Prompt: ", key="input")

    # File uploader for image input
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = ""
    if uploaded_file is not None:
       image = Image.open(uploaded_file)
       st.image(image, caption="Uploaded Image", use_column_width=True)

    # Submit button
    submit = st.button("Tell me about the image")

    if submit:
        if uploaded_file is not None:
            response = image_to_text_chatbot(input_text, uploaded_file)  # Call the chatbot function
            st.subheader("The response is:")
            st.write(response)
        else:
            st.warning("Please upload an image.")