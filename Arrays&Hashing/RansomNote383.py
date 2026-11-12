class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = [0] * 26

        for ch in ransomNote:
            letters[ord(ch) - ord('a')] += 1

        for ch in magazine:
            letters[ord(ch) - ord('a')] -= 1

        for val in letters:
            if val > 0:
                return False

        return True
