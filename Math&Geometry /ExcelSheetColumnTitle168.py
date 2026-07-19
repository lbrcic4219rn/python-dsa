class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber:
            columnNumber -= 1
            res = chr(columnNumber % 26 + ord('A')) + res
            columnNumber //= 26

        return chr(columnNumber + ord('A')) + res
