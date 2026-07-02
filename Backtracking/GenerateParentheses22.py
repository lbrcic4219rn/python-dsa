from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_used, close_used, curr):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if open_used < n:
                dfs(open_used + 1, close_used, curr + "(")

            if close_used < open_used:
                dfs(open_used, close_used + 1, curr + ")")

        dfs(0, 0, "")
        return res
