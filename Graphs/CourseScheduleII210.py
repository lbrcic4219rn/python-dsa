from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for c, p in prerequisites:
            prereq[c].append(p)
        res = []

        cycle, visited = set(), set()

        def dfs(i):
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for p in prereq[i]:
                if not dfs(p):
                    return False
            visited.add(i)
            res.append(i)
            cycle.remove(i)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
