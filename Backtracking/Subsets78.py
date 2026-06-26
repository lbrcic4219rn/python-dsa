from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, currSeq):
            if i == len(nums):
                res.append(currSeq[:])
                return

            currSeq.append(nums[i])
            dfs(i + 1, currSeq)
            currSeq.pop()
            dfs(i + 1, currSeq)

        dfs(0, [])
        return res
