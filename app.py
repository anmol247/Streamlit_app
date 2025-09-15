import streamlit as st

st.title("Welcome to My First Streamlit App!")
st.write("This is a simple website created using Streamlit.")

name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}! Glad you visited.")

button_clicked = st.button("Click Here!")
if button_clicked:
    st.write("Button clicked! Thanks for interacting.")
