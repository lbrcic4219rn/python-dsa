from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefixSum = [0] * len(words)
        prefixSum[0] = 1 if words[0][0] in vowels and words[0][len(words[0]) - 1] in vowels else 0
        for i in range(1, len(words)):
            valid = 1 if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels else 0
            prefixSum[i] = prefixSum[i - 1] + valid

        res = []

        for query in queries:
            if query[0] == 0:
                res.append(prefixSum[query[1]])
            else:
                res.append(prefixSum[query[1]] - prefixSum[query[0] - 1])

        return res
