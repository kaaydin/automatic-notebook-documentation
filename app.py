import streamlit as st
import streamlit.components.v1 as components
import nbformat
import json
from IPython.core.display import HTML
from streamlit_echarts import st_echarts
from nbconvert import HTMLExporter

from comment_generator import query_message_list
from utils import create_messagelist

st.set_page_config(layout="wide", page_title="Automatic Documentation for Jupyter Notebooks")

st.write("## Automatically generate documentation for your Jupyter Notebook")
st.write(":computer: Try uploading a Jupyter Notebook to watch how documentation is added magically. The adjusted notebook can be downloaded from the sidebar")
st.sidebar.write("## Upload and download :gear:")

def generate_new_notebook(upload):
    notebook = upload.read().decode("utf-8")

    col1.write("Original Notebook :camera:")
    col1_html = notebook
    components.html(col1_html, height=800)
    
    ## At this point, the notebook element is a string. We can try to turn it into a dictionairy:
    notebook_dict = json.loads(notebook)
    
    ## Access all code snippets and ########This is the format for accessing all of the code snippets. We can change the index in the second one to access the different
    ######## snippets based on their index:notebook_dict["cells"][0]["source"]
    ## And then pass this dictionairy to the create_messagelist. This will allows us to access all code cells
    
    messages = create_messagelist(notebook_dict)

    ## Query call to GPT-3.5
    GPT_return = query_message_list(messages)
    
    ## Instantiate new notebook
    nb = nbformat.v4.new_notebook()
    
    ## Add messages from GPT query to new notebook
    for message in GPT_return:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)

    ## 

    st.write("The notebook code")
    nb_true_quotes = json.dumps(nb, indent = 4) 

    
    st.write(nb_true_quotes)
    nb_encoded = str(nb_true_quotes).encode('utf-8')
    st.sidebar.download_button("Download documented notebook", nb_encoded, "documented_notebook.ipynb", "application/x-ipynb+json")

def display_notebook(notebook_data):
    html_exporter = HTMLExporter()
    notebook_html, _ = html_exporter.from_notebook_node(notebook_data)
    st.write(HTML(notebook_html), unsafe_allow_html=True)
    


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload a notebook", type=["ipynb"])

if my_upload:
    notebook_data = json.load(my_upload)
    display_notebook(notebook_data)
    generate_new_notebook(my_upload)

