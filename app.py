import streamlit as st
import nbconvert

from main import main

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")


# Download the fixed image

def render_notebook(notebook_path):
    with open(notebook_path, "r") as nb_file:
        nb_content = nb_file.read()

    html_exporter = nbconvert.HTMLExporter()
    notebook_html, _ = html_exporter.from_notebook_node(nbconvert.reads(nb_content, as_version=4))
    return notebook_html

def generate_new_notebook(upload):
    notebook = upload
    col1.write("Original Notebook :camera:")
    col1.render_notebook(notebook)

    adjusted_notebook = main(upload)
    col2.write("Fixed Image :wrench:")
    col2.render_notebook(adjusted_notebook)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", adjusted_notebook, "adjusted_notebook.ipynb", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["ipynb"])