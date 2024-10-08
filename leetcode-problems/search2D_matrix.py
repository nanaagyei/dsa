"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: 
matrix = 
[[1,2,4,8],
 [10,11,12,13],
 [14,20,30,40]], 
 
target = 10
Output: true

Example 2
Input: 
matrix = 
[[1,2,4,8],
 [10,11,12,13],
 [14,20,30,40]], 

target = 15
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: list[list], target: int) -> bool:
        pass