import requests

class OllamaClient:
    def __init__(self, model_name="llama3", base_url="http://localhost:11434/api"):
        self.model_name = model_name
        self.base_url = base_url

    def chat(self, system_prompt, user_message):
        url = f"{self.base_url}/chat"
        
        payload = {
            "model": self.model_name,
            "format": "json", # Força o Ollama a cuspir apenas JSON
            "stream": False,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        }
        
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["message"]["content"]

    def generate(self, prompt):
        url = f"{self.base_url}/generate"
        response = requests.post(url, json={"prompt": prompt})
        response.raise_for_status()
        return response.json()

    def list_tags(self):
        url = f"{self.base_url}/tags"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
