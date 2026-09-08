from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)

        maxOdd, maxEven = 0, 0
        for _, value in cnt.items():
            if value % 2 == 0:
                maxOdd = max(maxOdd, value)
            else:
                maxEven = max(maxEven, value)

        return maxOdd - maxEven
