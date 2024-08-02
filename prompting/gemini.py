import requests

# Sostituisci con la tua chiave API
api_key = ""

# Endpoint per generare del testo
endpoint = "https://api.gemini.com/v1/generate"

# Dati di input
data = {
    "prompt": "",
    "model": "gemini-1.5-flash"
}

# Intestazione della richiesta
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Effettua la richiesta POST
response = requests.post(endpoint, json=data, headers=headers)

# Controlla lo stato della risposta
if response.status_code == 200:
    # Analizza la risposta JSON
    result = response.json()
    print(result["generated_text"])
else:
    print("Errore:", response.text)
