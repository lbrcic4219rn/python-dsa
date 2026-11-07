from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        indx = 1
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                break
            indx += 1

        if indx == n:
            return True

        for i in range(indx + 1, indx + n):
            if nums[i % n - 1] > nums[i % n]:
                return False

        return True
