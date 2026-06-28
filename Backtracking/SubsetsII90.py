from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, currSeq):
            res.append(currSeq[:])

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                currSeq.append(nums[j])
                dfs(j + 1, currSeq)
                currSeq.pop()

        dfs(0, [])
        return res
