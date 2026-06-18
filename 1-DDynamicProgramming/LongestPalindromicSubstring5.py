class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def grow(l, r):
            nonlocal s, res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(res) < (r - l + 1):
                    res = s[l: r + 1]
                l -= 1
                r += 1

        for i in range(len(s)):
            grow(i, i)
            grow(i, i + 1)
        return res
