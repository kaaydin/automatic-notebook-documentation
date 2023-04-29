## Importing all relevant functions
import streamlit as st
import nbformat
import json
import base64
from nbconvert import HTMLExporter
from streamlit.components.v1 import html as st_html


from comment_generator import query_message_list
from utils import create_messagelist

## Setting website configurations
st.set_page_config(layout="wide", page_title="Automatic Documentation for Jupyter Notebooks")

## Writing title on website
st.write("## Automatically generate documentation for your Jupyter Notebook")

## Writing description text on website
st.write(":computer: Try uploading a Jupyter Notebook to watch how documentation is added magically. The adjusted notebook can be downloaded from the sidebar")

## Setting download sidebar
st.sidebar.write("## Upload and download :gear:")
my_upload = st.sidebar.file_uploader("Upload a notebook", type=["ipynb"])

## Setting to columns (left: old notebook; right: new notebook)
#col1, col2 = st.columns(2)
col1, col2 = st.columns(2)

## Function to define 

def generate_new_notebook(upload):
    
    ## Writing title for the first column 
    col1.write("Original notebook :camera:")
    
    ## Writing title for the second column
    col2.write("Updated notebook :camera:")

    ## Reading notebook in JSON-based format
    notebook_uploaded = upload.read().decode("utf-8")

    ## Turning original notebook into dictionary
    notebook_dict = json.loads(notebook_uploaded)

    ## Reading dictionary and creating message list
    messages = create_messagelist(notebook_dict)
    
    ## Create new notebook & fill 
    nb_new = nbformat.v4.new_notebook()

    for message in messages:
        message = message["content"]
        new_cell = nbformat.v4.new_code_cell(message)
        nb_new.cells.append(new_cell)

    html_exporter = HTMLExporter()
    (html_output_new, _) = html_exporter.from_notebook_node(nb_new)
    col1.write(st_html(html_output_new, height=800, scrolling=True))

    ## Query call to GPT-3.5
    GPT_return = query_message_list(messages)
    
    ## Instantiate new notebook
    nb = nbformat.v4.new_notebook()
    
    ## Add messages from GPT query to new notebook
    for message in GPT_return:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)

    ## 
    nb_true_quotes = json.dumps(nb, indent = 4) 
    nb_encoded = str(nb_true_quotes).encode('utf-8')

    html_exporter = HTMLExporter()
    (html_output, _) = html_exporter.from_notebook_node(nb)
    col2.write(st_html(html_output, height=800, scrolling=True))

    ## Creating download button with the updated notebook
    st.sidebar.download_button("Download documented notebook", nb_encoded, "documented_notebook.ipynb", "application/x-ipynb+json")


if my_upload:
    generate_new_notebook(my_upload)
else:
    st.write("Please upload a Jupyter Notebook to view.")


st.write("Hello Kaan, nice that we are working on this together :) ")



    ### Create visualiation of notebook
    #for message in messages:
    #    notebook_visualisation = message["content"]
    #    modified_string = notebook_visualisation.replace("\n ", "\n")
    #    col1.code(modified_string)