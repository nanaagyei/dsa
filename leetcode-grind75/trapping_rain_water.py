"""
Given n non-negative integers representing an 
elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1

        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]

        return res
