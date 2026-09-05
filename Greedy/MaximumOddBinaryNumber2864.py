class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        oneCnt = 0
        for i in range(n):
            if s[i] == "1":
                oneCnt += 1

        return (oneCnt - 1) * "1" + (n - oneCnt) * "0" + "1"