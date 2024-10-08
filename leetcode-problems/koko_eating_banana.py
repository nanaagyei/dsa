"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. 
Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. 
With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4
Output: 25
"""

import math


class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        # Brute Force
        k = max(piles)

        for i in range(1, max(piles) + 1):
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / i)
            if total_time <= h:
                k = min(i, k)

        return k

    def minEatingSpeed2(self, piles, h: int) -> int:
        # Binary Search
        def possible(k):
            return sum((p - 1) // k + 1 for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

    def minEatingSpeed3(self, piles, h: int) -> int:
        # Binary Search
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            if sum([math.ceil(p / mid) for p in piles]) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
