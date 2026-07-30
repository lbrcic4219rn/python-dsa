from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def canSplit(target):
            count = 1
            currSum = 0
            for num in nums:
                if currSum + num > target:
                    count += 1
                    currSum = 0
                currSum += num
            return count <= k

        while l < r:
            m = l + (r - l) // 2
            if canSplit(m):
                r = m
            else:
                l = m + 1
        return l
