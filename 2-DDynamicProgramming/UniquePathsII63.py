from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dp = [0] * COL
        dp[COL - 1] = 1

        for r in reversed(range(ROW)):
            for c in reversed(range(COL)):
                if grid[r][c] == 1:
                    dp[c] = 0
                    continue
                if c + 1 < COL:
                    dp[c] += dp[c + 1]
        return dp[0]
