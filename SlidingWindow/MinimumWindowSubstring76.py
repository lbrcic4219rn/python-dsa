class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount, window = {}, {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        minLen, minWindow = float("inf"), [-1, -1]
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in tCount and tCount[c] == window[c]:
                have += 1

            while have == need:
                if minLen > (r - l + 1):
                    minLen = r - l + 1
                    minWindow = [l, r]
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[minWindow[0]: minWindow[1] + 1] if minLen != float("inf") else ""
