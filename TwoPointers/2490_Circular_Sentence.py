class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        parts = sentence.split(" ")
        N = len(parts)

        firstPart0 = parts[0][0]
        lastPartN = parts[N - 1][len(parts[N - 1]) - 1]
        if firstPart0 != lastPartN:
            return False

        for i in range(1, N):
            lastPrev = parts[i - 1][len(parts[i - 1]) - 1]
            firstCurr = parts[i][0]
            if lastPrev != firstCurr:
                return False

        return True
