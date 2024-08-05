"""
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. If there are more than one such triplet,
return the sum of the triplet with the smallest sum.
"""

import math

class Solution:
    def threeSumClose(self, arr: list, target: int) -> int:
        arr.sort()
        smallest_diff = math.inf 
        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1
            
            while left < right:
                target_diff = target - arr[i] - arr[left] - arr[right]
                if target_diff == 0:
                    return target
                
                if (abs(smallest_diff) > abs(target_diff)) or (abs(smallest_diff) == abs(target_diff) and target_diff > smallest_diff):
                    smallest_diff = target_diff

                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        
        return target - smallest_diff