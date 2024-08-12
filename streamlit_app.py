import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBiw1y0RoSUfWy6ZiAOqOcyrWVYDmeJlF0")

model = genai.GenerativeModel('gemini-1.5-flash')

st.title("WELCOME TO LIORA APP")
st.write("LIORA APP IS A SIMPLE CHATBOT USING GEMMA 2B!")

input_text = st.text_input("You:", placeholder="Ask me anything!")

prompt = "{ROLE: Liora AI, INTRUCTIONS: Gunakan bahasa non formal untuk mendapatkan ekspresi yang lebih menarik. dan berikan response yang tidak panjang. } | MESSAGE: "

if input_text:
    response = model.generate_content(prompt + input_text)
    st.write("Bot:", response)

