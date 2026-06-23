from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = currMax = 1
        res = nums[0]

        for num in nums:
            tmp = currMax
            currMax = max(num * currMin, num * currMax, num)
            currMin = min(num * tmp, num * currMin, num)
            res = max(res, currMax)

        return res
