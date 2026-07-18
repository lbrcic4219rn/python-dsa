from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minCap = max(weights)

        def validateCapacity(cap):
            dayCount = 1
            currCount = 0
            for w in weights:
                if currCount + w > cap:
                    currCount = 0
                    dayCount += 1
                currCount += w
            return dayCount <= days

        l, r = minCap, sum(weights)

        while l < r:
            m = l + (r - l) // 2

            if validateCapacity(m):
                r = m
            else:
                l = m + 1

        return l
