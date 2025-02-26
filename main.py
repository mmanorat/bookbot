from stats import word_count, char_count, sort_on
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = word_count(text)
    character_counts = char_count(text)
    sorted_list = sort_on(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n\n----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("\n\n--------- Character Count -------")
    for char, count in sorted_list:
        print(f"{char}: {count}")
    print("============= END ===============")
main()
