class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and mappings[s[i]] < mappings[s[i + 1]]:
                res -= mappings[s[i]]
                continue
            res += mappings[s[i]]

        return res
