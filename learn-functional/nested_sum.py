def sum_nested_list(lst: list[int | list]) -> int:
    total_size = 0
    for item in lst:
        if isinstance(item,int):
            total_size += item
        elif isinstance(item,list):
            total_size += sum_nested_list(item)
        
    return total_size
test_input: list[int | list] = [5, [6, 7], [[8, 9], 10]]
print(sum_nested_list(test_input))
