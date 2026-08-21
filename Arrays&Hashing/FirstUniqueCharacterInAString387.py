class Solution:
    def firstUniqChar(self, s: str) -> int:
        valueIndex = {}
        unique = [True] * len(s)
        for i, ch in enumerate(s):
            if ch in valueIndex:
                unique[i] = False
                unique[valueIndex[ch]] = False
                continue
            valueIndex[ch] = i

        for i in range(len(unique)):
            if unique[i]:
                return i
        return -1
