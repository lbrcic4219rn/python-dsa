from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            maxReach = nums[l]
            for i in range(l, r + 1):
                maxReach = max(maxReach, i + nums[i])

            l = r + 1
            r = maxReach
            res += 1

        return res
