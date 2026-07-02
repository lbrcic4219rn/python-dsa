from collections import defaultdict
from typing import List


class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points.keys():
            if abs(px - x) == abs(py - y) and px != x and py != y:
                res += (
                        self.points[(x, y)]
                        * self.points.get((x, py), 0)
                        * self.points.get((px, y), 0)
                )

        return res
