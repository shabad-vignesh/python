import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def generate_quote(prompt: str):
    if not api_key:
        print("Error: API key not found.")
        return None

    model_id = "gpt2"

    # ✅ CORRECT router endpoint
    api_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 50,
            "temperature": 0.9,
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]

        return result

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        print(f"Response body: {response.text if 'response' in locals() else 'No response'}")
        return None

if __name__ == "__main__":
    prompt = "Generate an inspirational quote about technology and innovation."
    quote = generate_quote(prompt)
    if quote:
        print("\nGenerated Quote:\n")
        print(quote)
