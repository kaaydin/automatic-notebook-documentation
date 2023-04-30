# notebook-commentgenerator

## To be reused later - do not run 

if source_notebook.cells:
    first_cell = source_notebook.cells[0]
else: 
    print("The notebook is empty")
    

must run pip install openai first

### TODOs

Jupyter Notebooks are widely used in the field of data science for interactive data analysis, visualization, and model development. However, one of the major challenges in using Jupyter Notebooks is the lack of automatic documentation generation. Currently, users have to manually write and format documentation for their notebooks, which can be time-consuming and error-prone.

The goal of this project is to develop a tool that automatically generates documentation for Jupyter Notebooks. The tool will extract information from the notebook, such as the code cells, markdown cells, and output cells, and use it to create a documentation file in a specified format (e.g., HTML, PDF, or Markdown). The generated documentation should include information about the purpose of the notebook, the data used, the methods applied, the results obtained, and any visualizations created.
