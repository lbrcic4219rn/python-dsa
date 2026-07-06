from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            takeBack = i
            while stack and stack[-1][1] > h:
                si, sh = stack.pop()
                res = max(res, (i - si) * sh)
                takeBack = si
            stack.append((takeBack, h))

        while stack:
            si, sh = stack.pop()
            res = max(res, (len(heights) - si) * sh)
        return res
