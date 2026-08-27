from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = currSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                currSum = 0
            currSum += nums[i]
            res = max(res, currSum)

        return res
