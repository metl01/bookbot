from stats import word_count
from stats import letter_count

def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    total_count = word_count(book_path)
    total_letters = letter_count(book_path)
    print(total_letters)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
