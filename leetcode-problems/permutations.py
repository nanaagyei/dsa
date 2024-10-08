"""
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [7]
Output: [[7]]
"""

# Solution 1
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]
        
        result = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                result.append(p[:i] + [nums[0]] + p[i:])
        return result
    
# Solution 2

class Solution2:

    def permute(self, nums: list[int]) -> list[list[int]]:
        
        perms = [[]]
        for n in nums:
            new_perm = []
            for p in perms:
                for i in range(len(p) + 1):
                    new_perm.append(p[:i] + [n] + p[i:])
            perms = new_perm
        return perms