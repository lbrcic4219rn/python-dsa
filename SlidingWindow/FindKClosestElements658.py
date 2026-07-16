from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = float("inf")
        res = [-1, -1]
        l = curr = 0
        for r in range(len(arr)):
            curr += abs(arr[r] - x)
            if r - l + 1 == k:
                if closest > curr:
                    closest = curr
                    res = [l, r]
                curr -= abs(arr[l] - x)
                l += 1

        return arr[res[0]: res[1] + 1]
