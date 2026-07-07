from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = l + (r - l) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + m - 1) // m

            if totalTime <= h:
                r = m
            else:
                l = m + 1

        return l
