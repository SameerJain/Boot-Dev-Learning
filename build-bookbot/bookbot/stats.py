def get_book_txt(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def convert_book_to_list(book_path:str) -> list[str]:
    word_list = get_book_txt(book_path).split()
    return word_list

def get_freq_letters(word_list:list[str]) -> dict[str,int]:
    pass

def get_num_words(book_path: str) -> int:
    num_words = convert_book_to_list(book_path) 
    return len(num_words)
