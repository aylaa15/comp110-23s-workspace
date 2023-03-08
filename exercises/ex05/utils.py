"""EX05 - 'list' Utility Functions."""
__author__ = "730386998"

def only_evens(nums: list[int]) -> list[int]:
    """returns list of integers, containing only the even elements of the input parameter"""
    output: list[int] = []

    for elem in nums:
        if elem % 2 == 0:
            output.append(elem)
    return output

def concat(list1: list[int], list2: list[int]) -> list:
    """returns a new list which contains all of the elements of the first list followed by all of the elements of the second list"""
    output: list[int] = []

    for num in list1:
        output.append(num)
    for num in list2:
        output.append(num)
    return output

def sub(nums: list[int], start_idx: list[int], end_idx: list[int]) -> list:
    """returns a list which is a subset of the given list between the start index and the end index - 1"""
    new_list: list[int] = []
    if start_idx < 0:
        start_idx = 0

    if end_idx > len(nums):
        end_idx = len(nums)

    if len(nums) == 0 or start_idx >= len(nums) or end_idx <= 0:
        return []

    for num in range(start_idx, end_idx):
        new_list.append(nums[num])
    return new_list
