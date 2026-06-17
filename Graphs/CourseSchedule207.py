from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if not preMap[course]:
                return True

            visited.add(course)
            for i in preMap[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
