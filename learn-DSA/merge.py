from typing import List 

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    size = len(nums)
    first_arr = nums[:size]
    second_arr = nums[size - 1:]
    merge_sort(first_arr)
    merge_sort(second_arr)
    

def merge(first: list[int], second: list[int]) -> list[int]:
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i+= 1
        else:
            final.append(second[j])
            j+= 1
        
    if i < len(first):
        final.append(first[i:])
    if j < len(second):
        final.append(second[j:])
    
    return final

test = [1,2,3,4,5,6,7,8]
print(test[5:])
