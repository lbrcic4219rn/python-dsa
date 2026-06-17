class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or prev > heights[r][c] or (r, c) in visited:
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for i in range(ROWS):
            dfs(i, 0, pacific, 0)
            dfs(i, COLS - 1, atlantic, 0)

        for j in range(COLS):
            dfs(0, j, pacific, 0)
            dfs(ROWS - 1, j, atlantic, 0)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res
