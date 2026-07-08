from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        posDiag = set()
        negDiag = set()
        column = set()
        board = [['.'] * n for _ in range(n)]

        def dfs(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for col in range(n):
                if col in column or col + row in posDiag or row - col in negDiag:
                    continue
                posDiag.add(row + col)
                negDiag.add(row - col)
                column.add(col)
                board[row][col] = "Q"
                dfs(row + 1)
                posDiag.remove(row + col)
                negDiag.remove(row - col)
                column.remove(col)
                board[row][col] = "."

        dfs(0)
        return res
