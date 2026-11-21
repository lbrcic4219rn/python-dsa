from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [float("inf")] * len(triangle)
        dp[0] = 0
        minPath = float("inf")

        for i in range(len(triangle)):
            for j in reversed(range(len(triangle[i]))):
                if j > 0:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
                else:
                    dp[j] += triangle[i][j]

                if i == len(triangle) - 1:
                    minPath = min(minPath, dp[j])

        return minPath
