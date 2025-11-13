import sys
from stats import get_num_words, get_char_count, get_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    word_count = get_num_words(filepath)
    char_count = get_report(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, num in char_count:
        print(f"{char}: {num}")



if __name__ == "__main__":
    main()


