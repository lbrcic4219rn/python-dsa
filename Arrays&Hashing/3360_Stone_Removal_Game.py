class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in reversed(range(11)):
            if i > n:
                if i % 2:
                    return True
                else:
                    return False
            n -= i

        return True