import json
import os
import zipfile
import random
import time

import streamlit as st
from screenshot import photographer

RESOURCES_FOLDER = "output"
EXAMPLE_JSON = {
    "urls": ["https://alessandrocalista.it", "https://digimetrica.com"]
}

def elaborate_screenshot(url: str) -> tuple[bool, str, str]:
    return photographer.screenshot(url, output_folder=RESOURCES_FOLDER)

def elaborate_screenshots_from_file(file) -> list[str]:
    paths = []
    try:
        json_data = json.load(file)
    except json.JSONDecodeError:
        st.error("Errore: il file caricato non è un JSON valido.")
        return paths

    if "urls" not in json_data or not isinstance(json_data["urls"], list):
        st.error("Errore: il file JSON deve contenere una chiave 'urls' con una lista di URL.")
        return paths

    for url in json_data["urls"]:
        status, message, path = elaborate_screenshot(url)
        if status and path:
            paths.append(path)

    return paths

def create_zip(paths: list, zip_name=f"archivio-{random.randint(1, int(time.time()))}") -> bytes:
    with zipfile.ZipFile(zip_name, "w") as z:
        for file_path in paths:
            arcname = os.path.relpath(file_path, RESOURCES_FOLDER)
            z.write(file_path, arcname)
    with open(zip_name, "rb") as f:
        bytes = f.read()
        os.remove(zip_name)
        return bytes

def handle_single_url():
    input_url = st.session_state.input_url
    status, message, path = elaborate_screenshot(input_url)
    st.session_state.single_url_status = status
    st.session_state.single_url_message = message
    st.session_state.single_url_path = path

def handle_file_upload():
    input_file = st.session_state.json_file
    paths = elaborate_screenshots_from_file(input_file)
    if paths:
        st.success(f"{len(paths)} screenshot elaborati con successo.")
        zip_bytes = create_zip(paths)
        st.download_button(
            label="Scarica archivio ZIP",
            icon="📦",
            data=zip_bytes,
            file_name="archivio.zip",
            mime="application/zip",
            use_container_width=True
        )
    else:
        st.warning("Nessuno screenshot è stato elaborato. Controlla il file JSON.")

st.header("Elabora URL singolo")
st.text_input(label="Inserisci URL", key="input_url")
st.button(label="Elabora", icon="🧑🏻‍💻", on_click=handle_single_url, type="primary", use_container_width=True)

st.header("Carica un file JSON con multipli URL")
st.write("Puoi caricare un file JSON per elaborarlo. Qui sotto un esempio di formato atteso:")
st.code(json.dumps(EXAMPLE_JSON, indent=2), language='json')
file = st.file_uploader(label="Carica un file JSON", type=["json"], key="json_file")

if file:
    st.button(label="Elabora File", use_container_width=True, icon="🗂️", on_click=handle_file_upload)

if st.session_state.get("single_url_status"):
    if st.session_state.single_url_status:
        st.success(st.session_state.single_url_message)
        st.image(st.session_state.single_url_path, use_container_width=True)
        with open(st.session_state.single_url_path, "rb") as screenshot:
            st.download_button(
                label="Scarica immagine",
                icon="📥",
                data=screenshot,
                file_name="screenshot.jpg",
                mime="image/jpeg",
                use_container_width=True
            )
    else:
        st.error(st.session_state.single_url_message)
