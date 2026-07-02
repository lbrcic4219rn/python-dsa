class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = [0] * 26
        s2Map = [0] * 26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord("a")] += 1
            s2Map[ord(s2[i]) - ord("a")] += 1

        count = 0
        for i in range(26):
            if s1Map[i] == s2Map[i]:
                count += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if count == 26:
                return True

            c = ord(s2[r]) - ord("a")
            s2Map[c] += 1
            if s2Map[c] - 1 == s1Map[c]:
                count -= 1
            elif s2Map[c] == s1Map[c]:
                count += 1
            c = ord(s2[l]) - ord("a")
            s2Map[c] -= 1
            if s2Map[c] + 1 == s1Map[c]:
                count -= 1
            elif s2Map[c] == s1Map[c]:
                count += 1
            l += 1

        return count == 26