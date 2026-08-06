def get_book_txt(book_path: str) -> str:
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_list(file_contents: str) -> list[str]:
    return file_contents.split()

def get_char_freqs_Counter(file_contents: str) -> dict[str, int]:
    from collections import Counter

    return dict(Counter((file_contents)))

def get_char_freqs_iter(file_contents: str) -> dict[str, int]:
    freq_map = {}
    for char in file_contents:
        cleaned_char = char.lower()
        freq_map[cleaned_char] = freq_map.get(cleaned_char, 0) + 1
    return freq_map

def sort_on(char_freq:tuple[str,int]) -> int:
    return char_freq[1]

def chars_dict_to_sorted_list(char_freqs:dict[str,int]) -> list[tuple[str,int]]:
    result = []
    for key in char_freqs.keys():
        result.append(char_freqs[key])
    return sorted(result,reverse=False,key=sort_on)

'''
sorted exercise for new assigment 
return sorted new datatype
'''
