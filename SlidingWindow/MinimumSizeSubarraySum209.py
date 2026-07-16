from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minWindow = len(nums)
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minWindow = min(minWindow, r - l + 1)
                currSum -= nums[l]
                l += 1

        return minWindow if minWindow != len(nums) else 0
