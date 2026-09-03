from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        indx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[indx] = nums[i]
                indx += 1
        for i in range(indx, len(nums)):
            nums[i] = 0
