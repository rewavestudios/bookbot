from stats import get_num_words, count_characters, sort_char_counts

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def main():
    # Get the text from the book
    book_text = get_book_text("books/frankenstein.txt")

    # Count words
    num_words = get_num_words(book_text)

    # Count characters
    char_count = count_characters(book_text)

    # Sort characters
    sorted_char_count = sort_char_counts(char_count)

    # Print report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_info in sorted_char_count:
        print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")

main()
