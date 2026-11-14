import unittest
import importlib.util
from pathlib import Path

_client_path = Path(__file__).with_name("llm_client.py")
_spec = importlib.util.spec_from_file_location("llm_client", _client_path)
if _spec is None or _spec.loader is None:
    raise ImportError(f"Cannot load LLMClient from {_client_path}")
_client_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_client_module)
LLMClient = _client_module.LLMClient

# Fake provider for testing
class FakeProvider:

    def generate(self, prompt):
        return "AI stands for Artificial Intelligence."

class TestLLMClient(unittest.TestCase):

    def test_generate(self):

        provider = FakeProvider()
        client = LLMClient(provider)

        result = client.generate("Explain AI")

        self.assertEqual(
            result,
            "AI stands for Artificial Intelligence."
        )

if __name__ == "__main__":
    unittest.main()
