# Week 2 – Ollama

## Overview
This folder contains an LLM client exercise with a provider choice. The program asks the user to choose `gemini` or `ollama`, then accepts a question and prints the LLM response.

## Files
- `main.py` – entry point; prompts for the provider and the user's question.
- `llm_client.py` / `llm-client.py` – LLM client-related files visible in the project.
- `test-client.py` – client test file visible in the project.
- `requirements.txt` – Python dependencies.
- `.env` – local configuration, if required.
- `__pycache__/` – Python-generated cache files.

## Setup
Activate the shared virtual environment from the project root:

```powershell
& "C:\Users\praks\Downloads\GEN-AI\.venv\Scripts\Activate.ps1"
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run
From this folder:

```powershell
python main.py
```

When prompted:
1. Choose `gemini` or `ollama`.
2. Enter a question.
3. Read the response printed in the terminal.

## Notes
- Ollama must be installed and running locally if you select the Ollama provider.
- Keep credentials in `.env`; never commit secrets.
