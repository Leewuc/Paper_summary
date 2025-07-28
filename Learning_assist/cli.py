import argparse

from .pdf_utils import extract_text_from_pdf, split_text
from .gpt_summary import summarize_with_gpt


def summarize_pdf(pdf_path: str, output_format: str = "txt", api_key: str = "") -> None:
    """Summarize a PDF and write the result to a file."""
    raw_text = extract_text_from_pdf(pdf_path)
    chunks = split_text(raw_text)

    summaries = []
    for chunk in chunks:
        summary = summarize_with_gpt(chunk, api_key=api_key)
        if summary:
            summaries.append(summary)

    final_summary = "\n\n".join(summaries)
    if output_format == "txt":
        with open("summary.txt", "w") as f:
            f.write(final_summary)
    elif output_format == "md":
        with open("summary.md", "w") as f:
            f.write(f"# Paper Summary\n\n{final_summary}")
    else:
        raise ValueError("Unsupported format: %s" % output_format)
    print("Summary completed!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize PDF papers with OpenAI GPT")
    parser.add_argument("--pdf", type=str, required=True, help="Path to PDF file")
    parser.add_argument("--format", type=str, default="txt", help="Output format: txt or md")
    parser.add_argument("--api-key", type=str, default="", help="OpenAI API key")
    args = parser.parse_args()
    summarize_pdf(args.pdf, args.format, args.api_key)


if __name__ == "__main__":
    main()
