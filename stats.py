def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents

def get_num_words(filepath):
    return len(get_book_text(filepath).split())

def get_char_count(filepath):
    counted_chars = {}
    chars = list(get_book_text(filepath).lower())
    for char in chars:
        if char not in counted_chars:
            counted_chars[char] = 1
        else:
            counted_chars[char] += 1
    return counted_chars

def sort_on(item):
    return item[1]
    

def get_report(filepath):
    c = list(get_char_count(filepath).items())
    c.sort(reverse=True, key=sort_on)
    chars = []
    for i in range(len(c)):
        char = c[i][0]
        if char.isalpha():
            chars.append(c[i])
    return chars

