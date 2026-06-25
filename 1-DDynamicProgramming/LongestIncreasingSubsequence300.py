from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            maxSub = 0
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    maxSub = max(maxSub, dp[j])
            dp[i] = 1 + maxSub
            res = max(res, dp[i])

        return res
