import streamlit as st
from huggingface_hub import InferenceClient
import transformers

client = InferenceClient(
    "google/gemma-2-2b-it",
    token="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",
)

# Judul dan deskripsi aplikasi
st.title("WELCOME TO LIORA APP")
st.write("LIORA APP IS A SIMPLE CHATBOT USING GEMMA 2B!")

input_text = st.text_input("You:", placeholder="Ask me anything!")

prompt = "{ROLE: Liora AI, INTRUCTIONS: Gunakan bahasa non formal untuk mendapatkan ekspresi yang lebih menarik. dan berikan response yang tidak panjang. } | MESSAGE: "

if input_text:
        
    for message in client.chat_completion(
            messages=[{"role": "user", "content": prompt + input_text}],
            max_tokens=500,
            stream=True,
        ):
        response = message.choices[0].delta.content, end=""
        st.write("Bot:", response)