class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}

        best = -1
        for i, ch in enumerate(s):
            if ch in dic:
                best = max(best, i - dic[ch] - 1)
            else:
                dic[ch] = i
        return best
