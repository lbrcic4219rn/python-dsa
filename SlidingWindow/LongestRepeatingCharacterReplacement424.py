class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            ch = s[r]
            count[ch] = count.get(ch, 0) + 1
            maxFreq = max(maxFreq, count[ch])

            if (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
