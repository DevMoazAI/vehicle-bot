# llm/llm_query.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("GROQ_API_ENDPOINT")
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL_NAME")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Load the system prompt
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def get_response_from_llm(user_input):
    try:
        payload = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 600
        }

        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()

        data = response.json()
        return data['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f" Error contacting GROQ API: {str(e)}"
