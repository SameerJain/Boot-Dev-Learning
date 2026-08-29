def swap_case(char: str):
    if len(char) > 0:
        # print(f"string: {char}")
        if char[0] == "-":
            del char
    return


from collections.abc import Iterator


def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter: lambda )


document = "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n"

expected = "\n* We are the music makers\n* Come with me and you'll be\n"

print(remove_invalid_lines(document))
print(expected)