from abc import ABC, abstractmethod
from google import genai
import json
import urllib.request

# Common interface
class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass

# Gemini cloud provider
class GeminiProvider(LLMProvider):

    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        return response.text

# Ollama local provider
class OllamaProvider(LLMProvider):

    def __init__(self, model="llama3.2"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        request = urllib.request.Request(
            self.url,
            data=json.dumps({
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        with urllib.request.urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))["response"]

# Common client
class LLMClient:

    def __init__(self, provider):
        self.provider = provider

    def generate(self, prompt):
        return self.provider.generate(prompt)
