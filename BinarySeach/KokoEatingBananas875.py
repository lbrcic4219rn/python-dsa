from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            totalTime = 0
            for p in piles:
                totalTime += (p + m - 1) // m

            if totalTime <= h:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
