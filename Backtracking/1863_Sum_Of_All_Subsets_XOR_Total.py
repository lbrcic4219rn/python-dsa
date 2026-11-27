from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(i, curr):
            nonlocal res
            if i == len(nums):
                res += curr
                return

            backtrack(i + 1, curr ^ nums[i])
            backtrack(i + 1, curr)

        backtrack(0, 0)
        return res
