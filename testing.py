import google.generativeai as genai
import streamlit as tv
MY_PRIVATE_KEY = "AIzaSyDfQwNJz0NYOXv8bdu8RjXjoEeWjq_Ao_0" 

genai.configure(api_key=MY_PRIVATE_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') # 1.5-flash is still active in 2026

tv.write("---")
tv.header("🤖 Assistant: Secure Connection")

user_input = tv.chat_input("Bhai, is the new key working?")

if user_input:
    with tv.spinner("Talking to Gemini..."):
        try:
            response = model.generate_content(user_input)
            with tv.chat_message("assistant"):
                tv.write(response.text)
        except Exception as e:
            tv.error(f"Error: {e}")
