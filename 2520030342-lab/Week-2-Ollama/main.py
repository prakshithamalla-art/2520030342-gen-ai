import os
import importlib.util
import sys
from pathlib import Path

try:
    load_dotenv = importlib.import_module("dotenv").load_dotenv
except ImportError:
    def load_dotenv(*args, **kwargs):
        return False

_module_path = Path(__file__).with_name("llm_client.py")
_module_spec = importlib.util.spec_from_file_location("llm_client", _module_path)
if _module_spec is None or _module_spec.loader is None:
    raise ImportError(f"Could not load llm_client from {_module_path}")

_llm_client = importlib.util.module_from_spec(_module_spec)
sys.modules["llm_client"] = _llm_client
_module_spec.loader.exec_module(_llm_client)

GeminiProvider = _llm_client.GeminiProvider
OllamaProvider = _llm_client.OllamaProvider
LLMClient = _llm_client.LLMClient

load_dotenv(override=True)

provider_name = input(
    "Choose provider (gemini/ollama): "
).strip().lower()

if provider_name == "gemini":

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found in .env")

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":

    provider = OllamaProvider("llama3.2")

else:
    raise ValueError("Invalid provider selected")

client = LLMClient(provider)

prompt = input("Enter your question: ")

answer = client.generate(prompt)

print("\nLLM Response:")
print(answer)
