class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = [0] * 26

        for i in range(len(s)): 
            map[ord(s[i]) - ord('a')] += 1
            map[ord(t[i]) - ord('a')] -= 1

        for val in map: 
            if val != 0:
                return False
        return True