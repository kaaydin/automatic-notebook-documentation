import nbformat
import openai
from tqdm import tqdm

from comment_generator import run_api
from utils import read_notebook, create_notebook, save_notebook, write_notebook, create_messagelist


PATH = "/Users/kaanaydin/Desktop/apl-project/test_notebook.ipynb" ## To be changed at the end

API_KEY = "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"
openai.api_key = API_KEY

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0

INSTRUCTION = {"role": "system", "content": """"
        You are a helpful coding assistant that will take as input a cell from a Jupyter notebook and generate 
        an appropriate comment for the cell at the beginning. Some further instructions to keep in mind: Please keep the 
        generated comment to a maximum of 30 words. Ensure that the comments start with a '#' character and provide 
        clear explanations without modifying the code itself. Also, very important, include the code as part of the output. """}

source_notebook = read_notebook(PATH)
messages = create_messagelist(source_notebook) 

outputs = []

for message in tqdm(messages):
    output = run_api(chosen_model = MODEL, instruction = INSTRUCTION, message = message, temperature=TEMPERATURE)
    outputs.append(output)

new_notebook = create_notebook()

write_notebook(new_notebook, outputs)

save_notebook(new_notebook, "new_notebook.ipynb")

print("Done")