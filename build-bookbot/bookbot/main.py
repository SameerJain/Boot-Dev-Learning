import sys
import os
from stats import *
from prints import * 

def get_user_option(input_dict: dict[str,str]) -> int:
    for key,value in input_dict.items():
        print(f"{key}:{value}")
    user_input = input("\nEnter the corresponding Value:\n")
    return user_input


# Reference Function
def orginal_main_function():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    return sys.exit(1)

    book_path = sys.argv[1]
    generate_report(book_path)


def menu_based_main_function():
    if len(sys.argv) >= 3:
        print(
            "Usage:\nBasic: python3 main.py <path_to_book(ex: books/frankenstein.txt)>\nAdvanced: python3 main.py (Then follow the menu instructions)"
        )
        sys.exit(1)
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        print_report(book_path)
        sys.exit(1)

    print(
        "Welcome to the Samatron "
        "Bookbot"
        "!\nAll books are grabbed from the /books folder\n"
    )

    while True:
        books_list = os.listdir("books")
        options = {}
        for i in range(0, len(books_list)):
            options[str(i + 1)] = books_list[i]
        print('Select which "book" (.txt file) you would like to get stats of:')
        user_input = get_user_option(options)
        book_name = books_list[int(user_input) - 1]

        book_path = "books/" + book_name
        file_contents = get_book_txt(book_path)
        word_list = get_word_list(file_contents)
        char_freqs = get_char_freqs_iter(file_contents)
        sorted_char_freqs = create_sorted_dict_list(char_freqs)

        while True:
            print(f"\n\nEnter which stat you would like for {book_name}:")
            options = {
                "1": "Total amount of words",
                "2": "Total amount of characters",
                "3": "Frequency of each word",
                "4": "Get the standard report",
                "0": "Cancel",
            }
            user_input = get_user_option(options)
            print("\n\n")
            if user_input == "1":
                print(
                    f"Total number of words in {book_name} is {print_num_words(word_list)}"
                )
            elif user_input == "2":
                print(
                    f"Total number of characters in {book_name} is {sum(char_freqs.values())}"
                )
            elif user_input == "3":
                print_sorted_dict_list(sorted_char_freqs)
            elif user_input == "4":
                print_report(book_path)
            elif user_input == "0":
                break

        print("\nWould you like to try another book or quit?")
        options = {"1": "Try another book", "0": "Quit Program Instead"}
        user_input = get_user_option(options)
        if user_input == "0":
            print("Exiting Program...")
            sys.exit(1)


def main() -> None:
    # if len(sys.argv) < 2:
    #     print("Usage: python3 main.py <path_to_book>")
    #     return sys.exit(1)

    book_path = "books/frankenstein.txt"

    file_contents = get_book_txt(book_path)
    word_list = get_word_list(file_contents)
    char_freqs = get_char_freqs_iter(file_contents)
    sorted_char_freqs = chars_dict_to_sorted_list(char_freqs)

    print_num_words(word_list)
    print(sorted_char_freqs)

if __name__ == "__main__":
    main()
