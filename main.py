from stats import word_count
from stats import character_count
from stats import sorted_count
import sys

#Main Function
def main():
    #prints how to use if no file path is given
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    total_count = f"Found {word_count(text)} total words"
    total_letters = character_count(text)
    sorted_list = sorted_count(total_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(total_count)
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

#Open entire file as string stored to file_contents
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
