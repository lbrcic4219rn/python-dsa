from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                rank[p1] += 1
                parent[p2] = p1
            else:
                rank[p2] += 1
                parent[p1] = p2
            return 1

        count = n
        for u, v in edges:
            count -= union(u, v)
        return count