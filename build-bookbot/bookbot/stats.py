def get_book_txt(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def convert_book_to_list(file_contents:str) -> list[str]:
    word_list = file_contents.split()
    return word_list

def get_freq_letters(word_list:list[str]) -> dict[str,int]:
    pass

def get_num_words(word_list: list[str]) -> int:
    return len(word_list)
