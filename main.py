from stats import get_num_words, get_char_count, get_report 

def main():
    word_count = get_num_words()
    char_count = get_report()
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, num in char_count:
        print(f"{char}: {num}")



if __name__ == "__main__":
    main()


