"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.
"""

class Solution:
    def sorted_squares(self, arr):
        n = len(arr)

        left = 0
        right = n - 1

        squares = [0] * n

        highest_sq_idx = n - 1

        while left <= right:

            left_sq = arr[left] * arr[left]
            right_sq = arr[right] * arr[right]

            if left_sq > right_sq:
                squares[highest_sq_idx] = left_sq
                left += 1
            else:
                squares[highest_sq_idx] = right_sq
                right -= 1

            highest_sq_idx -= 1

        return squares