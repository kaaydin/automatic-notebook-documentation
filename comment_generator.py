import openai

API_KEY = "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"
openai.api_key = API_KEY

MODEL = "gpt-3.5-turbo"

INSTRUCTION = {"role": "system", "content": """"
        You are a helpful coding assistant that will take as input a cell from a Jupyter notebook and generate 
        an appropriate comment for the cell at the beginning. Some further instructions to keep in mind: Please keep the 
        generated comment to a maximum of 30 words. Ensure that the comments start with a '#' character and provide 
        clear explanations without modifying the code itself. Also, very important, include the code as part of the output. """}

def run_api(message, chosen_model=MODEL, instruction=INSTRUCTION):
  """
  This function runs an OpenAI chat completion model with the given message and instruction. The chosen model can be specified, 
  otherwise a default model is used. The output is the generated text from the model with a temperature of 0. The code creates 
  an instance of the ChatCompletion class and returns the content of the first message in the first choice of the output. 
  """
  output = openai.ChatCompletion.create(
    model = chosen_model,
    messages=[instruction,
              message],
    temperature = 0,
  )
  
  output_text = output.choices[0]["message"]["content"]
  return output_text

def query_message_list(messages):
  """
  This function takes a list of messages and queries an API with each message, returning a list of the API's responses.
  The API is called with a chosen model and instruction, and the message is formatted as a dictionary with a "role" key
  set to "user" and a "content" key set to the message. The API response is then appended to a list and returned. 
  """
    
  documented_messages = []

  for message in messages:
    queried_message = {"role": "user", "content": f'{message}'}
    documented_message = run_api(chosen_model = MODEL, instruction = INSTRUCTION, message = queried_message)
    documented_messages.append(documented_message)

  return documented_messages