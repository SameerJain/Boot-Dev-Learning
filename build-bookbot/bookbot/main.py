from stats import *

def print_num_words(num_words: int)-> str:
    return print(f"Found {num_words} total words")

def print_freq_letters(freq_letters: dict[str,int])->None:
    for key,value in freq_letters.items():
        print(f"'{key}': value")


def main():

    # Read File Challenge
    num_words = get_num_words(
        convert_book_to_list(get_book_txt("books/frankenstein.txt"))
    )
    print_num_words(
        get_num_words(convert_book_to_list(get_book_txt("books/frankenstein.txt")))
    )

    freq_letters = get_freq_letters()

if __name__ == "__main__":
    main()
