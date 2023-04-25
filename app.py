import streamlit as st
import streamlit.components.v1 as components
import nbconvert
import nbformat
import json

from comment_generator import query_message_list
from utils import read_notebook, create_notebook, save_notebook, write_notebook, create_messagelist, correct_spacing

st.set_page_config(layout="wide", page_title="Automatic Documentation for Jupyter Notebooks")

st.write("## Automatically generate documentation for your Jupyter Notebook")
st.write(
    ":computer: Try uploading a Jupyter Notebook to watch how documentation is added magically. The adjusted notebook can be downloaded from the sidebar"
)
st.sidebar.write("## Upload and download :gear:")

def generate_new_notebook(upload):
    notebook = upload.read().decode("utf-8")
    
    col1.write("Original Notebook :camera:")
    col1_html = notebook
    components.html(col1_html, height=800)
    #At this point, the notebook element is a string. We can try to turn it into a dictionairy:
    st.write("As a dictionairy")
    notebook_dict = json.loads(notebook)
    ########This is the format for accessing all of the code snippets. We can change the index in the second one to access the different
    ######## snippets based on their index:notebook_dict["cells"][0]["source"]
    st.write(notebook_dict["cells"][1]["source"])
    #And then pass this dictionairy to the create_messagelist. This will allows us to access all code cells
    messages = create_messagelist(notebook_dict)
    nb = nbformat.v4.new_notebook()

    for message in messages:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)



    #col2.write("Documented Notebook :wrench:")
    #col2_html = render_notebook(adjusted_notebook)
    #components.html(col2_html, height=800)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download documented notebook", nb, "documented_notebook.ipynb", "application/x-ipynb+json")

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload a notebook", type=["ipynb"])

if my_upload:
    generate_new_notebook(my_upload)