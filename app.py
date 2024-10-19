# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv # type: ignore

load_dotenv()  # take environment variables from .env.

import streamlit as st # type: ignore
import os
import pathlib
import textwrap

import google.generativeai as genai # type: ignore

from IPython.display import display # type: ignore
from IPython.display import Markdown # type: ignore


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)