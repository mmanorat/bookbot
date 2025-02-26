def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_counts = {}
    text = text.lower()

    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def sort_on(char_counts):
    sorted_list = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_list
