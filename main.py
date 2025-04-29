import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Define endpoint and headers
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}

# Define your prompt
prompt_text = '''
Write a friendly, professional email introducing CycesX to an Indian business owner who sells products internationally.
The email should:
- Explain how CycesX helps them easily receive payments from international clients.
- Mention specific pain points like high bank fees or delayed payments.
- Suggest a next step like visiting our website or scheduling a call.
- Maintain a tone that builds trust and shows understanding of their needs.
'''

# Define payload
payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt_text}
            ]
        }
    ]
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check and print the output
if response.status_code == 200:
    result = response.json()
    # Extract the actual response text
    generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
    print("\nGenerated Email:\n")
    print(generated_text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
