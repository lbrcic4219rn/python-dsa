from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        next = [[] for _ in range(n)]
        for u, v in edges:
            next[u].append(v)
            next[v].append(u)

        visits = set()

        def dfs(node, prev):
            if node in visits:
                return False

            visits.add(node)
            for nei in next[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visits) == n