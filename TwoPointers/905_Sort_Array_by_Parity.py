from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [0] * len(nums)

        for num in nums:
            if num % 2:
                res[r] = num
                r -= 1
            else:
                res[l] = num
                l += 1

        return res
