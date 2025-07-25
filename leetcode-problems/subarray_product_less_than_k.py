"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = 1
        left = 0
        count = 0

        for right, num in enumerate(nums):
            product *= num

            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1

        return count

# class Solution2: # Dynamic Programming Approach
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         if k <= 1:
#             return 0

#         n = len(nums)
#         dp = [0] * n
#         product = 1
#         for i in range(n):
#             product *= nums[i]
#             if product < k:
#                 dp[i] = i + 1
#             else:
#                 for j in range(i, -1, -1):
#                     product //= nums[j]
#                     if product < k:
#                         dp[i] = j + 1
#                         break
#         return sum(dp)
