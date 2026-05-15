def cout_words(book_text):
    words = book_text.split()
    total =len(words)
    return "Found " + str(total) + " total words."
def count_characters(book_text):
    fr = {}
    book_text = book_text.lower()
    for char in book_text:
        if char.isalpha():
            if char in fr:
                fr[char] += 1
            else:
                fr[char] = 1
    return fr
def get_char_in_desc_order(fr):
    sorted_fr = sorted(fr.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_fr:
        print(f"{char}: {count}")