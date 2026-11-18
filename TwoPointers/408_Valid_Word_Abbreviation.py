from curses.ascii import isdigit


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            if not isdigit(abbr[j]):
                return False

            if abbr[j] == '0':
                return False

            skip = 0
            while j < len(abbr) and isdigit(abbr[j]):
                skip = skip * 10 + int(abbr[j])
                j += 1
            i += skip

        return i == len(word) and j == len(abbr)
