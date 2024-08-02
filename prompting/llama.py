import requests

# Imposta la tua API key di Hugging Face
api_key = ''

# Definisci l'endpoint dell'API di Hugging Face per LLaMA
api_url = 'https://api-inference.huggingface.co/models/llama-model-name'  # Modifica con il nome reale del modello

# Definisci il prompt e altri parametri
prompt = ""
max_tokens = 50
temperature = 0.7

# Prepara il payload della richiesta
payload = {
    'inputs': prompt,
    'parameters': {
        'max_new_tokens': max_tokens,
        'temperature': temperature
    }
}

# Imposta le intestazioni della richiesta
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Fai una chiamata all'API
response = requests.post(api_url, json=payload, headers=headers)

# Controlla se la richiesta è andata a buon fine
if response.status_code == 200:
    # Estrai e stampa la risposta
    response_json = response.json()
    print(response_json['generated_text'])
else:
    # Gestisci eventuali errori
    print(f"Errore: {response.status_code} - {response.text}")
