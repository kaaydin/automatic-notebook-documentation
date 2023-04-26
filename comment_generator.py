import openai
from tqdm import tqdm

API_KEY = "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"
openai.api_key = API_KEY

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0

INSTRUCTION = {"role": "system", "content": """"
        You are a helpful coding assistant that will take as input a cell from a Jupyter notebook and generate 
        an appropriate comment for the cell at the beginning. Some further instructions to keep in mind: Please keep the 
        generated comment to a maximum of 30 words. Ensure that the comments start with a '#' character and provide 
        clear explanations without modifying the code itself. Also, very important, include the code as part of the output. """}

def run_api(message, chosen_model=MODEL, instruction=INSTRUCTION, temperature = TEMPERATURE):
  output = openai.ChatCompletion.create(
    model = chosen_model,
    messages=[instruction,
              message],
    temperature = 0,
  )
  
  output_text = output.choices[0]["message"]["content"]
  return output_text

def query_message_list(messages):
    outputs = []

    for message in tqdm(messages):
      output = run_api(chosen_model = MODEL, instruction = INSTRUCTION, message = message, temperature=TEMPERATURE)
      #output = output.replace('"', '"')
      output = output.replace("'", "\'") #New line
      outputs.append(output)

    return outputs