import sys
from stats import *
from prints import * 


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    book_path = sys.argv[1]
    generate_report(book_path)


if __name__ == "__main__":
    main()

    """
    MENU TEXT FOR LATER 
    "Welcome to the Samatron "Bookbot"!\nAll books are grabbed from the /books folder\nSelect which book (.txt file) you would like to get stats of:" 

    0: Recheck the /books folder 
    QUIT
    "Now enter which stat you would like:"
    Total amount of words
    Total amount of characters
    Frequency of each word 
    Frequency of each character

    Select a different book
    QUIT
    """
