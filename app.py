

## Importing all relevant functions
import streamlit as st
import nbformat
import json
from nbconvert import HTMLExporter

from comment_generator import query_message_list
from utils import create_messagelist

## Setting website configurations
st.set_page_config(layout="wide", page_title="Automatic Documentation for Jupyter Notebooks")
col1, col2 = st.columns(2)

## Writing title on website
st.write("## Automatically generate documentation for your Jupyter Notebook")

## Writing description text on website
st.write(":computer: Try uploading a Jupyter Notebook to watch how documentation is added magically. The adjusted notebook can be downloaded from the sidebar")

## Setting download sidebar
st.sidebar.write("## Upload and download :gear:")
my_upload = st.sidebar.file_uploader("Upload a notebook", type=["ipynb"])


## Function to define 

def generate_new_notebook(upload):
    
    ## Reading notebook as OTF
    notebook = upload.read().decode("utf-8")

    ## Writing title for the first column 
    col1.write("Original notebook :camera:")
    
    ## Writing title for the second column
    col2.write("Updated notebook :camera:")

    #col1_html = notebook
    #components.html(col1_html, height=800)

    
    ## Turning original notebook into dictionary
    notebook_dict = json.loads(notebook)

    ## Reading dictionary and creating message list
    messages = create_messagelist(notebook_dict)

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
    
    
    ## Creating download button with the updated notebook
    st.sidebar.download_button("Download documented notebook", nb_encoded, "documented_notebook.ipynb", "application/x-ipynb+json")


if my_upload:
    generate_new_notebook(my_upload)
else:
    st.write("Please upload a Jupyter Notebook to view.")



# col1_html = notebook
    # components.html(col1_html, height=800)


        ## Access all code snippets and ########This is the format for accessing all of the code snippets. We can change the index in the second one to access the different
    ######## snippets based on their index:notebook_dict["cells"][0]["source"]
    ## And then pass this dictionairy to the create_messagelist. This will allows us to access all code cells