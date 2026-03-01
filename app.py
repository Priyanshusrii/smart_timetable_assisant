import streamlit as st

# This sets the title of your web page
st.set_page_config(page_title="Smart Timetable")

st.title("🤖kya re ai")
st.write("Hello Team! Our chatbot starts here.")

# Simple input box to test
name = st.text_input("What is your name?")
if name:
    st.write(f"Welcome to the project, {name}!")
