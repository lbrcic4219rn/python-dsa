from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, targ, currSeq):
            if targ == 0:
                res.append(currSeq.copy())
                return

            for j in range(i, len(nums)):
                num = nums[j]
                if targ >= num:
                    currSeq.append(num)
                    backtrack(j, targ - num, currSeq)
                    currSeq.pop()

        backtrack(0, target, [])
        return res
