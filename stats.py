def get_book_text():
    with open("books/frankenstein.txt") as f:
        book_contents = f.read()
        return book_contents

def get_num_words():
    return len(get_book_text().split())

def get_char_count():
    counted_chars = {}
    chars = list(get_book_text().lower())
    for char in chars:
        if char not in counted_chars:
            counted_chars[char] = 1
        else:
            counted_chars[char] += 1
    return counted_chars

def sort_on(item):
    return item[1]
    

def get_report():
    c = list(get_char_count().items())
    c.sort(reverse=True, key=sort_on)
    chars = []
    for i in range(len(c)):
        char = c[i][0]
        if char.isalpha():
            chars.append(c[i])
    return chars

