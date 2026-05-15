import sys
from stats import cout_words, count_characters, get_char_in_desc_order
print("Usage: python3 main.py <path_to_book>")
def get_book_text(book_path):
    with open(book_path, "r") as file:
        return file.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Get the book path from command line arguments
    book_text = get_book_text(book_path)
    #print(book_text)  # Print the characters of the book
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(cout_words(book_text))  # Print the word count
    #print(count_characters(book_text))  # Print the character frequency
    print("--------- Character Count -------")
    print(get_char_in_desc_order(count_characters(book_text)))  # Print the character frequency in descending order
    print("============= END ===============")
main()
