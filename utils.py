import nbformat

## Read existing notebook
def read_notebook(notebook_path):
    with open(notebook_path) as f:
        return nbformat.read(f, as_version=4)
    
## Instantiate new notebook
def create_notebook():
    nb = nbformat.v4.new_notebook()
    return nb

## Save new notebook
def save_notebook(notebook, notebook_path):
    with open(notebook_path, 'w') as f:
        nbformat.write(notebook, f)


## Write list into Jupyter cells
def write_notebook(notebook, messages):
    for message in messages:
        new_cell = nbformat.v4.new_code_cell(message)
        notebook.cells.append(new_cell)


## Put input cells in list
def create_messagelist(notebook):
    messages = []

    for i in range(len(notebook)-1):
        content_notebook = str(notebook.cells[i]["source"])
        content = {"role": "user", "content": f'{content_notebook}'}
        messages.append(content)

    return messages

def correct_spacing(code_list):
    code_list_updates = ["\n" if x==" " else x for x in code_list]

    return code_list_updates