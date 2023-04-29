## Importing all relevant functions
import streamlit as st
from streamlit.components.v1 import html as st_html

import nbformat
from nbconvert import HTMLExporter

import json


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

    with col1:
        st.header("Original notebook :camera:")
        st_html(html_output_new, height=800, scrolling=True)

    ## Query call to GPT-3.5
    GPT_return = query_message_list(messages)
    
    ## Instantiate new notebook
    nb = nbformat.v4.new_notebook()
    
    ## Add messages from GPT query to new notebook
    for message in GPT_return:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)

    html_exporter = HTMLExporter()
    (html_output, _) = html_exporter.from_notebook_node(nb)

    ## 
    nb_true_quotes = json.dumps(nb, indent = 4) 
    nb_encoded = str(nb_true_quotes).encode('utf-8')


    with col2:
        st.header("Updated notebook :camera:")
        st_html(html_output, height=800, scrolling=True)

    ## Creating download button with the updated notebook
    st.sidebar.download_button("Download documented notebook", nb_encoded, "documented_notebook.ipynb", "application/x-ipynb+json")


if my_upload:
    generate_new_notebook(my_upload)
else:
    st.write("Please upload a Jupyter Notebook to view.")

st.write("Hello Kaan, nice that we are working on this together :) ")
st.write("Hello Dave, also appreciate working with you :D")