import nbformat
import json
from nbconvert import HTMLExporter

## Read existing notebook
def read_notebook(notebook_path):
    with open(notebook_path) as f:
        return nbformat.read(f, as_version=4)

##
def read_notebook_st(upload):
    notebook_uploaded = upload.read().decode("utf-8")
    notebook_dict = json.loads(notebook_uploaded)

    return notebook_dict
    
## Instantiate new notebook
def create_notebook(messages):
    nb = nbformat.v4.new_notebook()
    for message in messages:
        new_cell = nbformat.v4.new_code_cell(message)
        nb.cells.append(new_cell)
    
    return nb

## Save new notebook
def save_notebook(notebook, notebook_path):
    with open(notebook_path, 'w') as f:
        nbformat.write(notebook, f)

## Save new notebook in Streamlit
def save_notebook_st(notebook):
    nb_true_quotes = json.dumps(notebook, indent = 4) 
    nb_encoded = str(nb_true_quotes).encode('utf-8')

    return nb_encoded

## 
def retrieve_html(notebook):
    html_exporter = HTMLExporter()
    (html_output, _) = html_exporter.from_notebook_node(notebook)

    return html_output

## Put input cells in list
def create_messagelist(notebook):
    messages = []

    for i in range(len(notebook)-1):
        content = correct_spacing(notebook["cells"][i]["source"])
        messages.append(content)

    return messages

## 
def correct_spacing(code_list):
    code_list_updates = ["\n " if x==" " else x for x in code_list]
    full_string = " ".join(code_list_updates)

    return full_string