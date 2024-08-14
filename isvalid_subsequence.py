"""
Given two non-empty arrays of integers, 
write a function that determines whether the second array is a subsequence of the first one.
"""


class Solution:
    def isValidSubsequence(self, array, sequence):
        left = 0
        while left < len(array):
            if sequence and array[left] == sequence[0]:
                sequence.pop(0)
            left += 1

        return not sequence