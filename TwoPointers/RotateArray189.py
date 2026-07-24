from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def rota(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k %= len(nums)
        rota(0, len(nums) - 1)
        rota(0, k - 1)
        rota(k, len(nums) - 1)
