from math import ceil
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(ceil(dist[i] / speed[i]))

        time.sort()

        for i in range(len(time)):
            if time[i] <= i:
                return i

        return len(dist)
