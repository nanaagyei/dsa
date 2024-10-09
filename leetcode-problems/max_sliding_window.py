"""
You are given an array of integers nums and an integer k. 
There is a sliding window of size k that starts at the left edge of the array. 
The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.

Example 1:

Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        # Brute Force
        # output = []

        # left = 0

        # for right in range(k - 1, len(nums)):
        #     if right + 1 < len(nums):
        #         subarray = nums[left: right + 1]
                
        #     else:
        #         subarray = nums[left:]
            
        #     output.append(max(subarray))
            
        #     left += 1
        # return output

        # Deque
        left = right = 0
        q = deque()
        output = []

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if left > q[0]:
                q.popleft()
            
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1

            right += 1

        return output
        