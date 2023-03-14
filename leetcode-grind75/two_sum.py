"""
Given an array of integers nums and an integer target, return 
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

# Solution 

class Solution:
    def twoSum(self, nums, target: int):
        nums_hash = {}

        for i, num in enumerate(nums):
            if (target - num) in nums_hash:
                return [nums_hash[target - num], i]
            else:
                nums_hash[num] = i