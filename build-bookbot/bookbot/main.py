from stats import get_num_words, count_letters

def print_num_words(num_words: list[str])-> str:
    return print(f"Found {num_words} total words")

def print_freq_letters(freq_letters: dict[str,int])->str:
    

def main():

    # Read File Challenge
    num_words = get_num_words("books/frankenstein.txt")
    print_num_words(num_words)


if __name__ == "__main__":
    main()
