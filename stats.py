from typing import TypedDict

#counts the words in the file and returns them as an integer
def word_count(file_contents: str) -> int:
        words = file_contents.split()
        return len(words)

#Count each character in the file
def character_count(file_contents:str ) -> dict[str, int]:
    counted_characters = {}
    for c in file_contents:
         lowered = c.lower()
         counted_characters[lowered] = counted_characters.get(lowered, 0) + 1
    return counted_characters
#Class for sorted dict
class CharacterCount(TypedDict):
    char: str
    num: int
#function for returning key value
def sort_on(letters):
    return letters["num"]

#sorts alphanumerical characters from largest to smallest
def sorted_count(letters: dict[str, int]) -> list[CharacterCount]:
    result = [] 
    for letter in letters:
        result.append({"char": letter, "num": letters[letter]})
    result.sort(reverse=True, key=sort_on)
    return result
