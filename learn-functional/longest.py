def find_longest_word(document: str, longest_word: str = "") -> str:
    if not document:
        return longest_word
    words = document.split(maxsplit=1)
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) == 2:
        return find_longest_word(words[1], longest_word)
    else:
        return longest_word


print(find_longest_word("How are you?"))
