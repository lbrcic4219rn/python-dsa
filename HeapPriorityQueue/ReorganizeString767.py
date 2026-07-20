import heapq
from collections import Counter, deque


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [(count[c], c) for c in count.keys()]
        heapq.heapify_max(maxHeap)
        q = deque()
        res = ""
        while maxHeap or q:
            if q and q[0][2] <= len(res):
                cnt, char, _ = q.popleft()
                heapq.heappush_max(maxHeap, (cnt, char))
            if not maxHeap:
                return ""
            else:
                cnt, char = heapq.heappop_max(maxHeap)
                res += char
                if cnt > 1:
                    q.append((cnt - 1, char, len(res) + 1))

        return res
