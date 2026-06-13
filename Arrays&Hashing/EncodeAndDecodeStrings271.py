from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for str in strs:
            res += f"{len(str)}#{str}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            start = i
            while s[i] != '#':
                i += 1
            wordLen = int(s[start:i])
            i += 1  # skip '#'
            res.append(s[i:i + wordLen])
            i += wordLen

        return res
