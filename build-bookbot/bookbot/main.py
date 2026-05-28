import sys
import os
from stats import *
from prints import * 

def print_books_dir() -> None:
    pass

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    print("Welcome to the Samatron ""Bookbot""!\nAll books are grabbed from the /books folder\nSelect which book (.txt file) you would like to get stats of:")
    
    books_list = os.listdir("books")
    books_menu = {}
    for i in range(0,len(books_list)):
        books_menu[i+1] = books_list[i]
    for key,value in books_menu.items():
        print(f"{key}: {value}")
        

    book_path = sys.argv[1]
    print_report(book_path)

    print()


if __name__ == "__main__":
    main()

    # 

    # 0: Recheck the /books folder 
    # QUIT
    # "Now enter which stat you would like:"
    # Total amount of words
    # Total amount of characters
    # Frequency of each word 
    # Frequency of each character
      Get the standard report

    # Select a different book
    # QUIT
    # """
