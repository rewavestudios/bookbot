import argparse
import os
import sys

from stats import (
    get_book_text,
    get_num_words,
    count_characters,
    sort_char_counts,
    print_report,
)


def main():
    """Parse CLI args, read the book file, compute stats, and print a report.

    This centralizes file IO in `stats.py` and uses `print_report` to avoid
    duplicating output logic.
    """
    parser = argparse.ArgumentParser(description="Bookbot — analyze plain-text books")
    parser.add_argument("book_path", help="Path to the book text file to analyze")
    args = parser.parse_args()

    book_path = args.book_path

    if not os.path.isfile(book_path):
        print(f"Error: The file '{book_path}' was not found or is not a regular file.")
        sys.exit(1)

    try:
        book_text = get_book_text(book_path)
    except Exception as exc:  # keep narrow in future if specific errors expected
        print(f"Error reading '{book_path}': {exc}")
        sys.exit(1)

    # Compute metrics
    word_count = get_num_words(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_char_counts(char_count)

    # Use the reusable report printer in stats.py
    print_report(book_path, word_count, sorted_char_count)


if __name__ == "__main__":
    main()
