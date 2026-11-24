# Week 3 – LLM Monitoring

## Overview
This folder contains an LLM monitoring exercise. The project includes a `UsageLogger` implementation that imports `MongoClient` from `pymongo`, indicating that MongoDB connectivity is part of the logging setup.

## Files
- `main.py` – program entry point.
- `usage_logger.py` – contains the `UsageLogger` code.
- `llm_client.py` – LLM client module.
- `requirements.txt` – Python dependencies.
- `.env` – local configuration.
- `venv/` and `__pycache__/` – environment/cache folders shown in the project.

## Setup
Activate the shared virtual environment from the project root:

```powershell
& "C:\Users\praks\Downloads\GEN-AI\.venv\Scripts\Activate.ps1"
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

If the `pymongo` import error still appears, install it directly:

```powershell
python -m pip install pymongo
```

## Run
From this folder:

```powershell
python main.py
```

## Troubleshooting
If you see `ModuleNotFoundError: No module named 'pymongo'`, install `pymongo` in the same active virtual environment used to run the program.

## Notes
- Configure any required database connection settings in `.env`.
- Do not commit credentials or connection strings.
- A successful package installation does not by itself guarantee that a MongoDB server or database connection is available; check the project's configuration if a connection error occurs.
