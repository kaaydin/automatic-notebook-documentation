## Importing all relevant modules
import streamlit as st
from streamlit.components.v1 import html as st_html

from utils import read_notebook_st, create_notebook, create_messagelist, retrieve_html, save_notebook_st
from comment_generator import query_message_list


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


def generate_new_notebook(upload):
    """
     This function turns an uploaded notebook into a dictionary, creates an HTML window, queries GPT-3.5, creates a new notebook, 
     and saves it for downloading. The original and updated notebooks are displayed with a download button. 

    """
    ## Turning upload into dictionary
    original_notebook = read_notebook_st(upload)

    ## Create HTML
    original_HTML = retrieve_html(original_notebook)

    ## Display uploaded notebook (in HMTL)
    with col1:
        st.header("Original notebook :notebook:")
        st_html(original_HTML, height=800, scrolling=True)

    ## Reading dictionary and creating message list
    original_messages = create_messagelist(original_notebook)
    
    ## Query call to GPT-3.5
    documented_messages = query_message_list(original_messages)
    
    ## Create new notebook & fill
    documented_notebook = create_notebook(documented_messages)

    ## Retreive new HMTL
    documented_HTML = retrieve_html(documented_notebook)

    ## Display new notebook (in HMTL)
    with col2:
        st.header("Updated notebook :notebook:")
        st_html(documented_HTML, height=800, scrolling=True)
    
    ## Save new notebook for downloading
    downloaded_notebook = save_notebook_st(documented_notebook)

    ## Creating download button with the updated notebook
    st.sidebar.download_button("Download documented notebook", downloaded_notebook, "documented_notebook.ipynb", "application/x-ipynb+json")

    
## Running application on Streamlit
if my_upload:
    generate_new_notebook(my_upload)
else:
    st.write("Please upload a Jupyter Notebook to view.")
