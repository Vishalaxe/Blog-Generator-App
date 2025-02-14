import streamlit as st
from transformers import pipeline

device=-1
# Initialize the Hugging Face pipeline for text generation
generator = pipeline(
    "text-generation", 
    model="gpt2",  # Using GPT-2, a non-gated public model
    tokenizer="gpt2", 
    device=device  # Same model for tokenizer
)

## Streamlit setup
st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', 
                             ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    # Form the input text with selected style and number of words
    blog_prompt = f"Write a blog for {blog_style} job profile for the topic {input_text} within {no_words} words."
    
    # Generate blog using Hugging Face model
    response = generator(blog_prompt, max_new_tokens=int(no_words))  # Use max_new_tokens instead of max_length
    st.write(response[0]['generated_text'])





