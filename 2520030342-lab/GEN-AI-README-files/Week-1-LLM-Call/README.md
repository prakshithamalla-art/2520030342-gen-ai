# Week 1 – LLM Call

## Overview
This folder contains the first LLM-calling exercise. The `main.py` program was run successfully and returned an AI-generated explanation of Artificial Intelligence.

## Files
- `main.py` – runs the LLM call.
- `.env` – local environment configuration, such as API credentials (if required).
- `.gitignore` – lists files Git should ignore.
- `.myenv` – environment-related folder shown in the project.

## Setup
The parent `GEN-AI` project uses a Python virtual environment. From the project root, activate it in PowerShell:

```powershell
& ".\.venv\Scripts\Activate.ps1"
```

Install the dependencies required by this week's code if they are not already installed.

## Run
From this folder:

```powershell
python main.py
```

## Expected result
The program sends a prompt to an LLM and prints the model's response in the terminal.

## Notes
- Keep API keys and other secrets in `.env`.
- Do not commit `.env` or share its contents publicly.
