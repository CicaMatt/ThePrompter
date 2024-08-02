import openai

api_key = 'key'
openai.api_key = api_key

# Parameters
prompt = ""
model = "gpt-4"  # Usa 'gpt-4' per il modello GPT-4
max_tokens = 50
temperature = 0.7

# API call
response = openai.Completion.create(
    model=model,  # Cambia 'engine' in 'model'
    prompt=prompt,
    max_tokens=max_tokens,
    temperature=temperature
)

# Response
print(response.choices[0].text.strip())
