from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    result = {}
    for file_type in file_extension_tuples:
        for types in file_type:
            for ending in types:
                print(ending)
    return lambda final: result.get(file_type, "Unknown")


file_extensions_tuples: list[tuple[str, list[str]]] = [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])]

file_type_getter(file_extensions_tuples)

temp: list[int] =                                  