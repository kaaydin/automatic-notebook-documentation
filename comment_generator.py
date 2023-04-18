import openai

def run_api(chosen_model, instruction, message, temperature = 0):
  output = openai.ChatCompletion.create(
    model = chosen_model,
    messages=[instruction,
              message],
    temperature = 0,
  )
  
  output_text = output.choices[0]["message"]["content"]
  return output_text