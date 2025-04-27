from stats import get_num_words

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

main()
