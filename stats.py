def word_count(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
        file_contents_list = file_contents.split()
        num_words = len(file_contents_list)
        return f"Found {num_words} total words"

def letter_count(filepath:str ):
    count = 0
    with open(filepath) as f:
        file_contents = f.read() 
        for c in file_contents:
            count += 1
            print(count)
