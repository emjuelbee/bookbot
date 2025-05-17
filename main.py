from stats import get_word_count, get_character_counts, create_dictionary
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return filecontents


def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    char_counts = get_character_counts(book_text)
    # print(f"{num_words} words found in the document")
    # print(char_counts)
    print(
        f"============ BOOKBOT ============ \nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {num_words} total words\n--------- Character Count -------")
    diction = create_dictionary(char_counts)
    for dic in diction:
        if dic["char"].isalpha():
            print(f"{dic['char']}: {dic['nums']}")


main()
