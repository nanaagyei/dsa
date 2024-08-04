########## Problem 1 #############
"""
Given an array of sorted numbers, move all non-duplicate number instances 
at the beginning of the array in-place. The non-duplicate numbers should 
be sorted and you should not use any extra space so that the solution 
has constant space complexity i.e., O(1)

Move all the unique number instances at the beginning of the array and
after moving return the length of the subarray that has no duplicate in it.
"""


class Solution:
    def moveElements(self, arr):
        next_non_duplicate = 1

        i = 0

        while i < len(arr):
            if arr[i] != arr[next_non_duplicate - 1]:
                arr[i], arr[next_non_duplicate] = arr[next_non_duplicate], arr[i]

                next_non_duplicate += 1

            i += 1
        
        return next_non_duplicate


############# Problem 2 ################
"""
Given an unsorted array of numbers and a target 'key', 
remove all instances of 'key' in-place and return the new length of the array.
"""

class Solution2:
    def removeElement(self, arr, key):
        nextElement = 0

        for i in range(len(arr)):
            if arr[i] != key:
                arr[nextElement] = arr[i]
                nextElement += 1
        
        return nextElement