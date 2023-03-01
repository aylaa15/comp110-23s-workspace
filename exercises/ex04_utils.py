"""EX04 - Utils."""
__author__ = "730386998"

def all(nums: list[int], target: int) -> bool:
    """True if all numbers in the given list match the target number. False otherwise, or if the list is empty. """
    i: int = 0 

    if len(nums) == 0:
        return False 
    
    while i <= len(nums) - 1:
        if nums[i] != target:
            return False 
        i = i + 1
    return True

def max(nums: list[int]) -> int:
    """Returns the largest number in the given list of integers. Raises ValueError if the list is empty. """
    if len(nums) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0  
    max_num: int = nums[0]
    
    while i <= len(nums) -1:
        if nums[i] > max_num:
            max_num = nums[i]
        i = i + 1
    return max_num
    
    
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if the two lists have the same elements at every index, and False otherwise. """
    i: int = 0 

    if len(list1) != len(list2):
        return False
    
    while i <= len(list1)- 1 and len(list2) - 1:
        if list1[i] != list2[i]:
            return False
        i = i + 1 
    return True 
