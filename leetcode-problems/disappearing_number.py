"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        curr = abs(nums[i])
        nums[curr - 1] = -abs(nums[curr - 1])

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))
