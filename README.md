# Automatic Documentation of Jupyter Notebooks

This project provides a tool that automatically generates documentation for Jupyter Notebooks, making it easier to understand and share your work. By extracting comments, markdown cells, and function docstrings, it creates comprehensive and formatted documentation.

## Introduction

Jupyter Notebooks are widely used in the field of data science for interactive data analysis, visualization, and model development. However, one of the major challenges in using Jupyter Notebooks is the lack of automatic documentation generation. Currently, users have to manually write and format documentation for their notebooks, which can be time-consuming and error-prone.

The goal of this project is to develop a tool that automatically generates documentation for Jupyter Notebooks. The tool will extract information from the notebook, specifically the code cells, and generate documentation for the code that was passed to the tool. Ultimately, the tool can be used by a programmer to write documentation automatically which they will only have to proof-read instead of manually writing it themselves. 

## Getting Started
All of the code that is needed to run this code can be found on the GitHub repository for this project (incl. the requirements file). The GPT API key was removed and future users will have to add their own in line six of the "comment_generator.py" file. 

This project can be run in two ways: Locally, by running the main.py file, or online on Streamlit via app.py. 

For running it locally, please follow the following steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/kaaydin/automatic-notebook-documentation
    cd automatic-notebook-documentation
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. To generate documentation for a notebook:

    ```bash
    python generate_docs.py --notebook path/to/your_notebook.ipynb
    ```

## Input preparation
Our tool works best with code chunks that do not contain any documentation or comments in them. For this reason, preparing any input and cleaning them of these elements is highly recommended. Also, due to the token limit of the GPT 3.5 model, some codes might need to be shortened for the tool to work. Further improvement could focus on how to split code cells to ensure that all notebooks independent of code cell length can be run. 

## Final remarks
Since this project was about building a tool that automatically writes code documentation, we used our own tool to write most of our documentation, with some small human adjustments. All of the Docstrings for the functions were generated using our tool on our own code. 
