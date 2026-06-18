from math import sqrt


class Solution(object):
    def arrangeCoins(self, n):
        return int(sqrt(2 * n + 0.25) - 0.5)
