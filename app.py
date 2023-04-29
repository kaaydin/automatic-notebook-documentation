## Importing all relevant functions
import streamlit as st
import nbformat
import json
from nbconvert import HTMLExporter

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
col1, col2 = st.columns(2)

## Function to define 

def generate_new_notebook(upload):
    
    ## Writing title for the first column 
    col1.write("Original notebook :camera:")
    
    ## Writing title for the second column
    col2.write("Updated notebook :camera:")

    ## Reading notebook in JSON-based format
    notebook = upload.read().decode("utf-8")

    ## Turning original notebook into dictionary
    notebook_dict = json.loads(notebook)

    ## Reading dictionary and creating message list
    messages = create_messagelist(notebook_dict)

    ## Create visualiation of notebook
    for message in messages:
        notebook_visualisation = message["content"]
        modified_string = notebook_visualisation.replace("\n ", "\n")
        col1.code(modified_string)

    ## Query call to GPT-3.5
    GPT_return = query_message_list(messages)
    
    ## Instantiate new notebook
    nb = nbformat.v4.new_notebook()
    
    ## Add messages from GPT query to new notebook
    for message in GPT_return:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)

    ## HELP
    nb_true_quotes = json.dumps(nb, indent = 4) 
    nb_encoded = str(nb_true_quotes).encode('utf-8')

    ## Second visualisation
    test_text = nb_encoded["cells"]
    col2.write(test_text)
    #col2.write(type(nb_true_quotes))
    #notebook_dict_edited2 = type(nb_encoded)
    #col2.write(type(nb_encoded))
    
    ## Creating download button with the updated notebook
    st.sidebar.download_button("Download documented notebook", nb_encoded, "documented_notebook.ipynb", "application/x-ipynb+json")


if my_upload:
    generate_new_notebook(my_upload)
else:
    st.write("Please upload a Jupyter Notebook to view.")


st.write("Hello Kaan, nice that we are working on this together :) ")