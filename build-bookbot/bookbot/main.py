from stats import *



def main():

    # Read File Challenge
    franken_word_list = get_word_list("books/frankenstein.txt")
    print_num_words(franken_word_list)
    freq_map = get_freq_letters_iter(get_book_txt("books/frankenstein.txt"))
    print_freq_letters(freq_map)

if __name__ == "__main__":
    main()
