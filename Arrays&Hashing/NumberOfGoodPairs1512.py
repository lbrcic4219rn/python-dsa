from typing import List, Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for v in counts.values():
            res += sum(range(v))
        return res
