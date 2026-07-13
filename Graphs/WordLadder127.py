from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        edges = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                edges[key].append(word)
        q = deque()
        q.append(beginWord)
        visited = set()
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                visited.add(word)
                for i in range(len(word)):
                    key = word[:i] + "*" + word[i + 1:]
                    for w in edges[key]:
                        if w not in visited:
                            q.append(w)
            res += 1

        return 0
