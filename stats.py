def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # make everything lowercase
    character_counts = {}
    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts
