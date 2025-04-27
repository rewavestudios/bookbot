import sys
from stats import get_num_words, count_characters, sort_char_counts

def get_book_text(filepath):
    # Reads the text from a file.
    with open(filepath, "r") as f:
        return f.read()

def main():
    # Check if the path to the book is provided in the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program with an error code if the argument is missing or incorrect

    # Get the book path from the command-line arguments
    try:
        book_path = sys.argv[1]
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)
    
    # Get the text from the book
    book_text = get_book_text(book_path)

    # Count words
    num_words = get_num_words(book_text)

    # Count characters
    char_count = count_characters(book_text)

    # Sort characters
    sorted_char_count = sort_char_counts(char_count)

    # Print report
    print("============ BOOKBOT ============")
    print("Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_info in sorted_char_count:
        print(f"{char_info['char']}: {char_info['num']}")
    
    print("============= END ===============")

# Ensure this runs only when this script is executed directly
if __name__ == "__main__":
    main()
