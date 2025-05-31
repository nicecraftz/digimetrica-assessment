import streamlit as st
from screenshot import photographer

RESOURCES_FOLDER = "output"

def get_screenshot():
    input_url = st.session_state.input_url
    if (input_url is None or len(input_url) == 0) or not photographer.is_valid_and_reachable(input_url):
        st.write("URL non valido!")
        return

    path = photographer.screenshot(input_url, output_folder=RESOURCES_FOLDER)
    st.image(path, use_container_width=True)

    with open(path, "rb") as screenshot:
        st.download_button(
            label="Scarica immagine",
            icon="📥",
            data=screenshot,
            file_name="screenshot.jpg",
            mime="image/jpeg"
        )

st.text_input(label="Inserisci URL", key="input_url")
st.button(label="Elabora", icon="🧑🏻‍💻", on_click=get_screenshot, type="primary")
