from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, currSeq):
            if i == len(s):
                res.append(currSeq[:])

            for r in range(i, len(s)):
                if not isPali(i, r):
                    continue
                currSeq.append(s[i: r + 1])
                dfs(r + 1, currSeq)
                currSeq.pop()

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        dfs(0, [])
        return res
