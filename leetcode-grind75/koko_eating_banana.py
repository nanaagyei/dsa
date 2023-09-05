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
