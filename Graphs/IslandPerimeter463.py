from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    q.append((r, c))
                    break
            if q:
                break

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        visited.add(q[0])

        perimeter = 0

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    perimeter += 1

                elif (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

        return perimeter
