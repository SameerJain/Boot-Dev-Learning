import sys
import os
from stats import *
from prints import * 

def print_books_dir() -> None:
    pass

def print_dict

def main() -> None:
    if len(sys.argv) < 1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    print("Welcome to the Samatron ""Bookbot""!\nAll books are grabbed from the /books folder\nSelect which book (.txt file) you would like to get stats of:")

    books_list = os.listdir("books")
    books_menu = {}
    for i in range(0,len(books_list)):
        books_menu[str(i+1)] = books_list[i]
    books_menu{"0":"QUIT"}
    for key,value in books_menu.items():
        print(f"{key}: {value}")

    value = input("Enter the corresponding Value")

    print("Now enter which stat you would like:")
    options = {"1": "Total amount of words",
               "2":"Total amount of characters",
               "3":"Frequency of each word",
               "4":"Get the standard report",
               "0": "QUIT"}

    book_path = "books/" + books_menu[value]
    print_report(book_path)

    print("Would you like to try another book or quit")


if __name__ == "__main__":
    main()

