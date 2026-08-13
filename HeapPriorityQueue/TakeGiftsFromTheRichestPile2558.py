import heapq

from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        for i in range(k):
            val = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, isqrt(val))

        res = 0
        for g in gifts:
            res += g

        return res
