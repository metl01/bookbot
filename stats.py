from typing import TypedDict

def word_count(file_contents: str) -> int:
        words = file_contents.split()
        return len(words)

def letter_count(file_contents:str ) -> dict[str, int]:
    counted_letters = {}
    for c in file_contents:
         lowered = c.lower()
         counted_letters[lowered] = counted_letters.get(lowered, 0) + 1
    return counted_letters

class CharacterCount(TypedDict):
    char: str
    num: int

def sort_on(letters):
    return letters["num"]

def sorted_count(letters: dict[str, int]) -> list[CharacterCount]:
    result = [] 
    for letter in letters:
        result.append({"char": letter, "num": letters[letter]})
        result.sort(reverse=True, key=sort_on)
    return result
