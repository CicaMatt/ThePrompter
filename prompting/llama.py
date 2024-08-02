import requests

api_key = ''

# Endpoint
api_url = 'https://api-inference.huggingface.co/models/llama-model-name'  # Modifica con il nome reale del modello

# Parameters
prompt = ""
max_tokens = 50
temperature = 0.7

# Request data
payload = {
    'inputs': prompt,
    'parameters': {
        'max_new_tokens': max_tokens,
        'temperature': temperature
    }
}

#
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# API call
response = requests.post(api_url, json=payload, headers=headers)

# Response
if response.status_code == 200:
    # Estrai e stampa la risposta
    response_json = response.json()
    print(response_json['generated_text'])
else:
    # Gestisci eventuali errori
    print(f"Errore: {response.status_code} - {response.text}")
