from typing import List, Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for v in counts.values():
            res += v * (v - 1) // 2
        return res
    