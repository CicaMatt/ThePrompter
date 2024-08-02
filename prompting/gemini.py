import requests

api_key = ""

# Endpoint
endpoint = "https://api.gemini.com/v1/generate"

# Input data
data = {
    "prompt": "",
    "model": "gemini-1.5-flash"
}

#
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Call
response = requests.post(endpoint, json=data, headers=headers)

# Response
if response.status_code == 200:
    # Analizza la risposta JSON
    result = response.json()
    print(result["generated_text"])
else:
    print("Errore:", response.text)
