from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            if nums[i] == 2 and i < right:
                nums[right], nums[i] = nums[i], nums[right]
                i -= 1
                right -= 1
            i += 1
