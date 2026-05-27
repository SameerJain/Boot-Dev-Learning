from main import get_book_txt

def count_words(input: str) -> int:
    num_words = get_book_txt(input).split()
    return f"Found {len(num_words)} total words"
