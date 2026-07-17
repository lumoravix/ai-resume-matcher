import streamlit as st

st.title("AI Resume Matcher")
st.write("Welcome! This app will compare a resume with a job description.")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}! Your AI project is ready.")