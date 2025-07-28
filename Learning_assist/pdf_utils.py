import fitz  # PyMuPDF
import tiktoken


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def split_text(text: str, max_tokens: int = 3000) -> list[str]:
    """Split text into chunks of roughly ``max_tokens`` tokens."""
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = encoder.decode(tokens[i:i + max_tokens])
        chunks.append(chunk)
    return chunks
