from typing import TypedDict
from stats import *


class CharacterCount(TypedDict):
    char: str
    num: int


def print_report(book_path: str) -> None:
    file_contents = get_book_txt(book_path)
    word_list = get_word_list(file_contents)
    char_freqs = get_char_freqs_iter(file_contents)
    sorted_char_freqs = create_sorted_dict_list(char_freqs)

    print("============ BOOKBOT ============")
    print(f"Analzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print_num_words(word_list)
    print("--------- Character Count ---------")
    print_sorted_dict_list(sorted_char_freqs)
    print("============ END ============")


def sort_key(CharacterCount) -> int:
    return CharacterCount["num"]


def create_sorted_dict_list(char_freqs: dict[str, int]) -> list[CharacterCount]:
    sorted_dict_list = []

    for key, value in char_freqs.items():
        char_dict: CharacterCount = {"char": key, "num": value}
        sorted_dict_list.append(char_dict)
    sorted_dict_list.sort(reverse=True, key=sort_key)
    return sorted_dict_list


def print_sorted_dict_list(sorted_dict_list: list[CharacterCount]) -> None:
    for char_dict in sorted_dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")


def print_num_words(word_list: list[str]) -> None:
    return print(f"Found {len(word_list)} total words")


def print_char_freqs(char_freqs: dict[str, int]) -> None:
    for key, value in char_freqs.items():
        print(f"'{key}': {value}")
