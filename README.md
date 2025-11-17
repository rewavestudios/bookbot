# Bookbot

Bookbot is a small command-line utility for analyzing plain-text books. It counts words and computes character frequency statistics (case-insensitive, letters only). The repository includes a few public-domain sample books in the `books/` folder so you can try the tool immediately.

**Features:**
- Word count for a book
- Character frequency analysis (letters only, case-insensitive)
- Simple, dependency-free Python code suitable for learning or small scripts

**Requirements:**
- Python 3.8+ (tested with Python 3.10+)

**Installation:**
1. Clone the repository:

```bash
git clone <repo-url>
cd bookbot
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

There are no external dependencies to install for the basic functionality.

**Usage:**

Run the analyzer by passing the path to a text file (one of the included books or your own text file):

```bash
python3 main.py books/frankenstein.txt
```

Example output (abbreviated):

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77,000 total words
--------- Character Count -------
e: 45000
t: 30000
a: 28000
...
============= END ===============
```

Notes:
- `main.py` is the CLI entry point. It reads a file, computes word count using `get_num_words`, counts alphabetic characters with `count_characters`, and prints a sorted list of character counts.
- `stats.py` contains reusable functions: `get_book_text`, `get_num_words`, `count_characters`, `sort_char_counts`, and `print_report`.

**Project structure:**

- `main.py` — CLI script to analyze a book file
- `stats.py` — core analysis functions
- `books/` — sample book text files (tracked in the repository)
	- `frankenstein.txt`
	- `mobydick.txt`
	- `prideandprejudice.txt`
- `.gitignore` — standard Python ignores (virtualenvs, caches)
- `README.md` — this file

**Development notes & suggestions:**
- The project purposely keeps dependencies minimal. If you add new dependencies, add a `requirements.txt` or `pyproject.toml`.
- Consider adding unit tests for `stats.py` (for example, using `pytest`) to validate counting logic and edge cases (empty files, punctuation-only content, non-ASCII characters).
- There is some duplicate functionality: both `main.py` and `stats.py` include a `get_book_text` helper — consider centralizing file IO in `stats.py` and having `main.py` import it.
- Download some more books from [Project Gutenberg](https://www.gutenberg.org/)! 

**Contributing**

Contributions are welcome. Please fork the repo, make changes on a feature branch, and open a pull request against `main`. If you add behavior or bug fixes, include tests and update the README with any new usage instructions.

**License**

See the [LICENSE](LICENSE) file for details.
