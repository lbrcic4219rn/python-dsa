from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, currSeq):
            if len(currSeq) == k:
                res.append(currSeq.copy())
                return

            for j in range(i, n + 1):
                currSeq.append(j)
                backtrack(j + 1, currSeq)
                currSeq.remove(j)

        backtrack(1, [])
        return res
