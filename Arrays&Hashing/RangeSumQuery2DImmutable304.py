from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix) + 1
        self.COLS = len(matrix[0]) + 1
        self.prefix = [[0] * self.COLS for _ in range(self.ROWS)]

        for i in range(1, self.ROWS):
            for j in range(1, self.COLS):
                self.prefix[i][j] = (
                        matrix[i - 1][j - 1]
                        + self.prefix[i - 1][j]
                        + self.prefix[i][j - 1]
                        - self.prefix[i - 1][j - 1]
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.prefix[row2 + 1][col2 + 1]
        topRight = self.prefix[row1][col2 + 1]
        bottomLeft = self.prefix[row2 + 1][col1]
        topLeft = self.prefix[row1][col1]
        return bottomRight - topRight - bottomLeft + topLeft