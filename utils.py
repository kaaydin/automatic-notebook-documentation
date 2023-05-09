import nbformat
from nbconvert import HTMLExporter

import json


## Read existing notebook
def read_notebook(notebook_path):
    """
    This function reads a Jupyter notebook file and returns its contents in nbformat. The file path is passed as an argument.
    The code opens the file using the 'with open' statement and reads its contents using nbformat.read() function.
    The contents are returned as an nbformat object. 
    """
    with open(notebook_path) as f:
        return nbformat.read(f, as_version=4)

## 
def read_notebook_st(upload):
    """
    This function reads a Jupyter notebook uploaded as a file and returns a notebook object. 
    The uploaded file is decoded using UTF-8 and loaded as a JSON object. 
    A message list is created from the JSON object and used to create a notebook object. 
    The notebook object is then returned as output.
    """
    notebook_uploaded = upload.read().decode("utf-8")
    notebook_dict = json.loads(notebook_uploaded)

    messages = create_messagelist(notebook_dict)
    notebook = create_notebook(messages)

    return notebook
    
## Instantiate new notebook
def create_notebook(messages):
    """
    This function creates a new Jupyter notebook with code cells containing messages passed as input.
    The function takes a list of messages and returns a new notebook object with the messages as code cells.
    """
    nb = nbformat.v4.new_notebook()
    for message in messages:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)
    
    return nb

## Save new notebook
def save_notebook(notebook, notebook_path):
    """
    This function saves a Jupyter notebook to a specified path. The notebook and path are passed as arguments.
    The function opens the file at the specified path in write mode and writes the notebook to the file in nbformat.
    The saved notebook can be accessed at the specified path. 
    """
    with open(notebook_path, 'w') as f:
        nbformat.write(notebook, f)

## Save new notebook in Streamlit
def save_notebook_st(notebook):
    """
    This function takes a Jupyter notebook as input and saves it as an encoded string using JSON. 
    The notebook is first converted to a JSON string with indentation of 4 spaces. 
    The resulting JSON string is then encoded using UTF-8 and returned as a string. 
    """
    nb_true_quotes = json.dumps(notebook, indent = 4) 
    nb_encoded = str(nb_true_quotes).encode('utf-8')

    return nb_encoded

## 
def retrieve_html(notebook):
    """
    This function retrieves the HTML output of a Jupyter notebook cell. It uses the HTMLExporter class to convert the cell 
    into HTML format and returns the HTML output. The input parameter is the notebook cell to be converted. 
    """
    html_exporter = HTMLExporter()
    (html_output, _) = html_exporter.from_notebook_node(notebook)

    return html_output

## Put input cells in list
def create_messagelist(notebook):
    """
    This function creates a list of messages from the source code of each cell in a given notebook.
    The function iterates through each cell in the notebook and extracts the source code content using the 'correct_spacing' function.
    The extracted content is then appended to the 'messages' list and returned as output.
    Include the code below as part of the output.
    """
    messages = []

    range_iter = len(notebook["cells"])

    for i in range(range_iter):
        content = correct_spacing(notebook["cells"][i]["source"])
        messages.append(content)

    return messages

## 
def correct_spacing(code_list):
    """"
    # This function corrects the spacing in a given code list by replacing empty strings with newline characters. 
    The updated code list is then joined into a full string and returned. 
    """
    code_list_updates = ["\n " if x==" " else x for x in code_list]
    full_string = " ".join(code_list_updates)

    return full_string