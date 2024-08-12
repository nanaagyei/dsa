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
