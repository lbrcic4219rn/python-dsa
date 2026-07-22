from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        prefixSum = 0
        prefixes[0] = 1
        res = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            res += prefixes[prefixSum - k]
            prefixes[prefixSum] += 1
        return res
