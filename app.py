import streamlit as st
import streamlit.components.v1 as components
import nbconvert
from main import main

st.set_page_config(layout="wide", page_title="Automatic Documentation for Jupyter Notebooks")

st.write("## Automatically generate documentation for your Jupyter Notebook")
st.write(
    ":computer: Try uploading a Jupyter Notebook to watch how documentation is added magically. The adjusted notebook can be downloaded from the sidebar"
)
st.sidebar.write("## Upload and download :gear:")

def render_notebook(notebook_content):
    html_exporter = nbconvert.HTMLExporter()
    notebook_html, _ = html_exporter.from_notebook_node(nbconvert.reads(notebook_content, as_version=4))
    return notebook_html

def generate_new_notebook(upload):
    notebook = upload.read().decode("utf-8")
    col1.write("Original Notebook :camera:")
    col1_html = render_notebook(notebook)
    components.html(col1_html, height=800)

    adjusted_notebook = main(notebook)
    col2.write("Documented Notebook :wrench:")
    col2_html = render_notebook(adjusted_notebook)
    components.html(col2_html, height=800)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download documented notebook", adjusted_notebook, "documented_notebook.ipynb", "application/x-ipynb+json")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload a notebook", type=["ipynb"])

if my_upload:
    generate_new_notebook(my_upload)
