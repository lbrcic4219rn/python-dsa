from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(indx, currSeq):
            if indx == len(nums):
                res.append(currSeq[:])

            for i in range(indx, len(currSeq)):
                currSeq[indx], currSeq[i] = currSeq[i], currSeq[indx]
                dfs(indx + 1, currSeq)
                currSeq[indx], currSeq[i] = currSeq[i], currSeq[indx]

        dfs(0, nums)
        return res
