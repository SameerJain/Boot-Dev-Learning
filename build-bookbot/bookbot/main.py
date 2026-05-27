from stats import *

def get_book_txt(input: str)->str:
    with open(input) as f:
        file_contents = f.read()
    return file_contents



def main():

    # Read File Challenge
    print(count_words("books/frankenstein.txt"))

main()
