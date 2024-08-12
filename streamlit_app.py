import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_id = "mistralai/Codestral-22B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Set up the Streamlit app layout
st.set_page_config(page_title="AI Text Generator", page_icon="✨", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #007bff;
    }
    </style>
    """, unsafe_allow_html=True
)

# App title and description
st.title("✨ AI Text Generator")
st.write("Generate text using advanced AI models. Enter your prompt and see the magic happen!")

# Text input from the user
text_input = st.text_input("Enter your prompt:", placeholder="Type something here...")

# Button to generate text
if st.button("Generate"):
    if text_input:
        # Tokenize and generate output
        inputs = tokenizer(text_input, return_tensors="pt")
        outputs = model.generate(**inputs, max_new_tokens=500)
        
        # Decode and display the output
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        st.subheader("Generated Text:")
        st.write(generated_text)
    else:
        st.warning("Please enter a prompt to generate text.")

# Footer
st.markdown(
    """
    ---
    http://exz.free.nf
    """
)
