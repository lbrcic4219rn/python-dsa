from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        if nums[l] != target:
            return [-1, -1]
        start = l

        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m

        return [start, l - 1]
