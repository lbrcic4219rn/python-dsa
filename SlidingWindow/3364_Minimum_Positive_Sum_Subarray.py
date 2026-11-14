from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        answer = float("inf")

        for size in range(l, r + 1):
            currSum = sum(nums[:size])
            if currSum > 0:
                answer = min(answer, currSum)

            for right in range(size, len(nums)):
                currSum += nums[right] - nums[right - size]
                if currSum > 0:
                    answer = min(answer, currSum)

        return answer if answer != float("inf") else -1
