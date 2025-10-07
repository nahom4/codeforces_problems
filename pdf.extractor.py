#!/usr/bin/env python3
"""
extract_pages.py

Usage:
    python extract_pages.py input.pdf start_page end_page --output out.pdf

Extracts pages from `input.pdf`, starting at page `start_page` up to `end_page` (inclusive),
and writes them into a new PDF `out.pdf`.

Pages are 1‑indexed (i.e. page 1 is the very first page of the PDF).
"""

import sys
import argparse
from PyPDF2 import PdfReader, PdfWriter

def extract_pages_to_pdf(pdf_path: str, start_page: int, end_page: int, output_path: str) -> None:
    """
    Open pdf_path, copy pages from start_page to end_page (inclusive),
    and write them to output_path.

    Note: start_page and end_page are 1-indexed.
    """
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    num_pages = len(reader.pages)

    if start_page < 1 or end_page < start_page or end_page > num_pages:
        raise ValueError(
            f"Page range must be between 1 and {num_pages}, and start_page ≤ end_page."
        )

    # Copy pages
    for p in range(start_page - 1, end_page):  # PdfReader pages are 0-indexed
        writer.add_page(reader.pages[p])

    # Write to output
    with open(output_path, "wb") as out_f:
        writer.write(out_f)


def main():
    parser = argparse.ArgumentParser(
        description="Extract pages from a PDF and save them to a new PDF file."
    )
    parser.add_argument(
        "input_pdf",
        help="Path to the input PDF file."
    )
    parser.add_argument(
        "start_page",
        type=int,
        help="First page to extract (1-indexed)."
    )
    parser.add_argument(
        "end_page",
        type=int,
        help="Last page to extract (1-indexed, ≥ start_page)."
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Output PDF file path."
    )
    args = parser.parse_args()

    try:
        extract_pages_to_pdf(args.input_pdf, args.start_page, args.end_page, args.output)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Extracted pages {args.start_page}–{args.end_page} to '{args.output}'.")

if __name__ == "__main__":
    main()
