# Week 6 – AutoRegression

## Aim
To execute an autoregressive text-generation program and observe how text is generated sequentially.

## Description
This experiment runs `autoregression.py` and displays generated text in the terminal. The observed output was:

```text
Generated Text:
the student worked hard the teacher taught students studied well the
```

Autoregressive generation produces text one step at a time. The next token is selected using the preceding text as context, and the generated token becomes part of the context for the following step.

## Files
- `autoregression.py` – Python program used for the experiment.

## Requirements
- Python 3
- Any Python packages imported by `autoregression.py`

## How to Run
1. Open PowerShell in the project environment.
2. Activate the virtual environment:

   ```powershell
   & "C:\Users\praks\Downloads\GEN-AI\.venv\Scripts\Activate.ps1"
   ```

3. Move into the Week 6 folder:

   ```powershell
   cd "C:\Users\praks\Downloads\GEN-AI\2520030342-lab\Week-6-AutoRegression"
   ```

4. Run the program:

   ```powershell
   python autoregression.py
   ```

## Observed Output

```text
Generated Text:
the student worked hard the teacher taught students studied well the
```

## Result
The autoregression program executed successfully and generated a sequence of text.

## Conclusion
The experiment demonstrated autoregressive text generation, where each generated token contributes to the context used to generate subsequent text.
