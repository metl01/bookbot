def main():
    book_path = "./books/frankenstein.txt"
    print(word_count(book_path))

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def word_count(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents_list = file_contents.split()
        num_words = len(file_contents_list)
        return f"Found {num_words} total words"

main()
