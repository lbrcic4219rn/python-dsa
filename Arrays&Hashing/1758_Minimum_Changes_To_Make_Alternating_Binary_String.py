class Solution:
    def minOperations(self, s: str) -> int:
        expected1 = "1"
        expected0 = "0"
        res1 = 0
        res0 = 0
        for ch in s:
            if ch != expected1:
                res1 += 1
            else:
                res0 += 1
            expected1 = "1" if expected1 == "0" else "0"
            expected0 = "1" if expected0 == "0" else "0"
        return min(res1, res0)
