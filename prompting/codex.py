import openai

api_key = ''
openai.api_key = api_key

# Parameters
prompt = ""
model = "code-davinci-002"
max_tokens = 50
temperature = 0.7

# API call
response = openai.Completion.create(
    model=model,  # Usa 'model' per specificare il modello
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature
)

# Response
print(response.choices[0].text.strip())