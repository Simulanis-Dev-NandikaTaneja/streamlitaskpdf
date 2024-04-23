import streamlit as st
from streamlitdemo import ask_question
st.set_page_config(page_title="Search From PDF", page_icon=":robot:")
st.header("Search your PDFS")

form_input = st.text_input('Enter Query')
submit = st.button("Generate")

if submit:
    st.write(ask_question(form_input))