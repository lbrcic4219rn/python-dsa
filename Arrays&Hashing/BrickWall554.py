from collections import defaultdict
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = defaultdict(int)
        maxGap = 0
        for row in wall:
            curr = 0
            for i in range(len(row) - 1):
                brick = row[i]
                curr += brick
                gaps[curr] += 1
                maxGap = max(maxGap, gaps[curr])

        return len(wall) - maxGap
