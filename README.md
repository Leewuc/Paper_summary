# Paper Summary

A simple command-line tool that summarizes research papers in PDF format using OpenAI's GPT models.

## Requirements

- Python 3.10 or higher
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [tiktoken](https://github.com/openai/tiktoken)
- [openai](https://github.com/openai/openai-python)

Install the dependencies with:

```bash
pip install PyMuPDF tiktoken openai
```

## Usage

```bash
python -m Learning_assist.llm_pdf --pdf path/to/paper.pdf --format md --api-key YOUR_API_KEY
```

The summary will be written to `summary.txt` or `summary.md` depending on the selected format.

## Project Structure

- `Learning_assist/pdf_utils.py` – PDF text extraction and token-based splitting
- `Learning_assist/gpt_summary.py` – helper to query the OpenAI API
- `Learning_assist/cli.py` – command-line interface and summarization workflow
- `Learning_assist/llm_pdf.py` – small wrapper to run the CLI module

## Example

```
python -m Learning_assist.llm_pdf --pdf sample.pdf --format txt --api-key sk-...
```

This command extracts the text from `sample.pdf`, summarizes it with GPT, and saves the result to `summary.txt`.
