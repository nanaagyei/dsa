"""
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4

Example 2:
Input: nums = [2,3,1,1,5,5,4], k = 3
Output: 4
"""

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
    

# Time complexity: O(nlogk)

# Space complexity: O(k)

if __name__ == "__main__":
    nums = [2,3,1,1,5,5,4]
    k = 3
    print(Solution().findKthLargest(nums, k))