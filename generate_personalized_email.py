import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Endpoint and headers
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}

# Step 1: Collect user inputs
business_owner_name = input("Enter Business Owner's Name: ")
your_name = input("Enter Your Name: ")
your_title = input("Enter Your Title (e.g., Business Development Manager): ")
website_link = input("Enter Website Link: ")
calendly_link = input("Enter Calendly (or Meeting) Link (Optional): ")
phone_number = input("Enter Your Phone Number (Optional): ")

# Step 2: Prepare dynamic prompt with user inputs
prompt_text = f'''
Write a friendly, professional email introducing CycesX to an Indian business owner who sells products internationally.

The email must:
- Address {business_owner_name} personally.
- Introduce CycesX as a solution for receiving international payments.
- Mention pain points like high bank fees, delayed settlements, and cashflow disruption.
- Highlight specific benefits like reducing fees by 30% and receiving payments 3x faster.
- Show how CycesX is better than traditional banks or platforms like Paypal.
- Include a next step: visiting {website_link} or scheduling a call at {calendly_link if calendly_link else 'N/A'}.
- Maintain an empathetic, supportive tone.
- Close with {your_name}'s signature, title ({your_title}), and optionally {phone_number}.
'''

# Step 3: Prepare payload
payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt_text}
            ]
        }
    ]
}

# Step 4: Call Gemini API
response = requests.post(url, headers=headers, json=payload)

# Step 5: Process and print the result
if response.status_code == 200:
    result = response.json()
    generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
    print("\nGenerated Personalized Email:\n")
    print(generated_text)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
