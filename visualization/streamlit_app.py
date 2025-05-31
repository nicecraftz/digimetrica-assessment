import streamlit as st


def get_screenshot(url: str):
    print("Hello World")

input = st.text_input(label="Inserisci URL")
st.button(label="Elabora",icon="🧑🏻‍💻", on_click=get_screenshot(input), type="primary")
