# Problem
# Given an integer array nums, return true if any value 
# appears at least twice in the array, and return false 
#if every element is distinct.


class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == 0:
            return False
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
    #############################################
    # another solution

    def containsDuplicate2(self, nums) -> bool:
        if len(nums)  == len(set(nums)):
            return False
        else:
            return True