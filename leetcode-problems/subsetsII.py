"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,1]
Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:
Input: nums = [7,7]
Output: [[],[7], [7,7]]
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        subsets = []

        def dfs(i):
            if i >= len(nums):
                result.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return result