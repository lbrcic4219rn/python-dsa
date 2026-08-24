from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        for i in range(len(nums)):
            sum1 = prefixSum[i - 1] if i > 0 else 0
            sum2 = prefixSum[len(nums) - 1] - prefixSum[i]
            if sum1 == sum2:
                return i
        return -1
