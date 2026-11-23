from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        res = 0
        for i in range(N):
            res += mat[i][i] + mat[N - i - 1][i]

        if N % 2:
            res -= mat[N // 2][N // 2]

        return res
