from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = Counter(arr)

        maxCnt = -1
        for k, v in cnt.items():
            if k == v:
                maxCnt = max(maxCnt, k)

        return maxCnt
