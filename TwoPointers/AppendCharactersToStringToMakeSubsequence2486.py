class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tIndx = 0
        for i in range(len(s)):
            if tIndx == len(t):
                return 0
            if s[i] == t[tIndx]:
                tIndx += 1

        return len(t) - tIndx
