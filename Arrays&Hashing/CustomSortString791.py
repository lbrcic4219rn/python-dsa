from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chCount = Counter(s)
        res = ""

        for ch in order:
            res += ch * chCount[ch]
            chCount[ch] = 0

        for key, value in chCount.items():
            if value == 0:
                continue
            res += key * value

        return res
