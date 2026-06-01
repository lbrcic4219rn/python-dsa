class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        groups = [0] * 26

        for i in range(len(s)): 
            groups[ord(s[i]) - ord('a')] += 1
            groups[ord(t[i]) - ord('a')] -= 1

        for val in groups:
            if val != 0:
                return False
        return True