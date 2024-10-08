"""
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [7]
Output: [[],[7]]
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        subsets = []

        def dfs(i):
            if i >= len(nums):
                result.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)
            subsets.pop()
            dfs(i + 1)
        dfs(0)
        return result