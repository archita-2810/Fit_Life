import streamlit as st
from app import run_chatbot_app  # Import the chatbot function
from vision import image_to_text_chatbot  # Import your image-to-text chatbot function
from diet_planner import diet_planner_app  # Import the diet planner function
from workout_planner import workout_planner_app  # Import the workout planner function
from PIL import Image

# Title of the web app
st.title("FitLife")

# Sidebar to choose between the four options
option = st.sidebar.selectbox(
    'Choose a solution for your healthy life',
    ('Text-to-Text Chatbot', 'Image-to-Text Chatbot', 'Diet Planner', 'Workout Planner')
)

# If the user selects Text-to-Text Chatbot
if option == 'Text-to-Text Chatbot':
    run_chatbot_app()  # Call the chatbot app function from app.py

# If the user selects Image-to-Text Chatbot
elif option == 'Image-to-Text Chatbot':
    st.header('Image-to-Text Chatbot')
    
    # File uploader to upload an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        
        if st.button('Submit'):
            # Call the image-to-text function
            response = image_to_text_chatbot(input_text="explain me what is written in the image", image=image)  # Call the function from vision.py
            st.write("Response: ", response)

# If the user selects Diet Planner
elif option == 'Diet Planner':
    st.header('Diet Planner')
    diet_planner_app()  # Call the diet planner function

# If the user selects Workout Planner
elif option == 'Workout Planner':
    st.header('Workout Planner')
    workout_planner_app()  # Call the workout planner function