from stats import count_words, count_characters_occurrences, sort_occurrences
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    count = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    occurrences = count_characters_occurrences(text)
    sorted = sort_occurrences(occurrences)

    for line in sorted:
        print(line["char"] + ": " + str(line["count"]))

    print("============= END ===============")



main()