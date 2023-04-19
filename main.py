import argparse

from comment_generator import query_message_list
from utils import read_notebook, create_notebook, save_notebook, write_notebook, create_messagelist


def main(args):
    source_notebook = read_notebook(args.input_file)
    messages = create_messagelist(source_notebook) 
    outputs = query_message_list(messages)
    new_notebook = create_notebook()
    write_notebook(new_notebook, outputs)
    save_notebook(new_notebook, "new_notebook.ipynb")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate comments for Jupyter notebook cells.")
    parser.add_argument("input_file", type=str, help="Path to the input Jupyter notebook.")
    args = parser.parse_args()
    main(args)