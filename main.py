import argparse

from utils import read_notebook, create_notebook, create_messagelist, save_notebook
from comment_generator import query_message_list


def main(args):
    
    ##
    original_notebook = read_notebook(args.input_file)
    
    ##
    original_messages = create_messagelist(original_notebook) 
    
    ##
    documented_messages = query_message_list(original_messages)
    
    ##
    documented_notebook = create_notebook(documented_messages)
    
    ##
    save_notebook(documented_notebook, "documented_notebook.ipynb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate comments for Jupyter notebook cells.")
    parser.add_argument("input_file", type=str, help="Path to the input Jupyter notebook.")
    args = parser.parse_args()
    main(args)