def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def get_num_words(book_text):
    # Split the text into words and count them
    words = book_text.split()
    return len(words)

def count_characters(text):
    # Create an empty dictionary to hold character counts
    char_count = {}

    # Loop through every character in the text
    for char in text.lower():  # Make sure characters are counted case-insensitively
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_char_counts(char_count):
    # Filter out non-alphabetical characters
    sorted_counts = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
    # Sort by 'num' in descending order
    sorted_counts.sort(reverse=True, key=lambda x: x["num"])
    return sorted_counts

def print_report(book_path, word_count, sorted_char_count):
    # Print the Bookbot report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_info in sorted_char_count:
        char = char_info["char"]
        count = char_info["num"]
        print(f"{char}: {count}")
    
    print("============= END ===============")
