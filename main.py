## Importing relevant modules
import argparse
from utils import read_notebook, create_notebook, create_messagelist, save_notebook
from comment_generator import query_message_list


def main(args):
    """
    This function processes a notebook file, extracts messages from it, queries the messages,
    creates a new notebook with the queried messages, and saves the new notebook as a separate file.
    """
    
    ## Read original notebook
    original_notebook = read_notebook(args.input_file)
    
    ## Create code blocks in list
    original_messages = create_messagelist(original_notebook) 
    
    ## Create documented code blocks
    documented_messages = query_message_list(original_messages)
    
    ## Create new notebook with documented code blocks
    documented_notebook = create_notebook(documented_messages)
    
    ## Save new notebook as a separate file
    save_notebook(documented_notebook, "documented_notebook.ipynb")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate comments for Jupyter notebook cells.")
    parser.add_argument("input_file", type=str, help="Path to the input Jupyter notebook.")
    args = parser.parse_args()
    main(args)
