"""
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
where i, j, and k are three different indices. 
Write a function to return the count of such triplets.
"""

class Solution:
    def threeSumLessThanTarget(self, arr, target):
        arr.sort()
        count = 0
        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1

            while left < right:
                threeSum = arr[i] + arr[left] + arr[right]


                if threeSum < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count

########## Example ##############
arr = [-1, 4, 2, 1, 3]
target = 5
soln = Solution()
print(soln.threeSumLessThanTarget(arr, target))