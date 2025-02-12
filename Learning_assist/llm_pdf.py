import fitz # PyMuPDF
import tiktoken
from openai import OpenAI, APIError

def extract_text_from_pdf(pdf_path):  # text extraction
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def split_text(text,max_tokens=3000): # text chunk division
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens = encoder.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk = encoder.decode(tokens[i:i+max_tokens])
        chunks.append(chunk)
    return chunks

def summarize_with_gpt(text, model="gpt-3.5-turbo"):
    client = OpenAI(api_key="")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a research assistant. Summarize this papaer in 3 paragraphs."},
                {"role": "user", "content": text}
            ]
        )
    except APIError as e:
        print(f"OpenAI API Error: {e}")
        return None
    return response.choices[0].message.content


def main(pdf_path, output_format="txt"):
    # 텍스트 추출
    raw_text = extract_text_from_pdf(pdf_path)

    # 텍스트 분할
    chunks = split_text(raw_text)

    # 각 청크 요약
    summaries = []
    for chunk in chunks:
        summary = summarize_with_gpt(chunk)
        if summary:
            summaries.append(summary)

    # 결과 저장
    final_summary = "\n\n".join(summaries)
    if output_format == "txt":
        with open("summary.txt", "w") as f:
            f.write(final_summary)
    elif output_format == "md":
        with open("summary.md", "w") as f:
            f.write(f"# Paper Summary\n\n{final_summary}")

    print("Summary completed!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str, required=True)
    parser.add_argument("--format", type=str, default="txt")
    args = parser.parse_args()

    main(args.pdf, args.format)

# python llm_pdf.py --pdf " " --format md