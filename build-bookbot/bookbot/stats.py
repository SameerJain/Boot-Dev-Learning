from typing import TypedDict 

class CharacterCount(TypedDict):
    char: str
    num: int

def print_report(book_path: str):
    print("============ BOOKBOT ============")
    print(f"Analzing book found at {book_path}...")
    print("----------- WORD COUNT -----------")
    print(Found {} total words)
    print(---------Character Count---------)
    print()
    print(============ END ============)
def print_num_words(word_list: list[str]) -> None:
    return print(f"Found {len(word_list)} total words")

def print_freq_letters(freq_letters: dict[str,int])->None:
    for key,value in freq_letters.items():
        print(f"'{key}': {value}")

def get_book_txt(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_list(book_path:str) -> list[str]:
    return get_book_txt(book_path).split()

def get_freq_letters_Counter(file_contents: str):
    from collections import Counter
    return dict(Counter((file_contents)))

def get_freq_letters_iter(file_contents:str):
    freq_map = {}
    for char in file_contents:
        cleaned_char = char.lower()
        freq_map[cleaned_char] = freq_map.get(cleaned_char,0)+ 1
    return freq_map

