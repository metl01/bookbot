from stats import word_count
from stats import letter_count
from stats import sorted_count

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    total_count = f"Found {word_count(text)} total words"
    total_letters = letter_count(text)
    sorted_list = sorted_count(total_letters)
    print(total_count)
    #print(total_letters)
    print(sorted_list)




def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


main()
