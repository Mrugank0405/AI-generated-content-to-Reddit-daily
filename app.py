import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("groq_api_key")

st.sidebar.title("Personalization")
prompt = st.sidebar.text_input("System Prompt: ", "Write an engaging post about AI.")
model = st.sidebar.selectbox(
    'Choose a model', ['Llama3-8b-8192', 'Llama3-70b-8192', 'Mixtral-8x7b-32768', 'Gemma-7b-It']
)

# Groq client
client = Groq(api_key=groq_api_key)

st.title("💬 Chat with Groq's LLM")

# Generate content
if st.button("Generate Content"):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=model,
    )
    st.write("Generated Content:")
    st.text(response.choices[0].message.content)
