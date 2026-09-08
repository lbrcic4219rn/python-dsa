from typing import List, Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        indx = 0
        for s in arr:
            if cnt[s] == 1:
                indx += 1
            if indx == k:
                return s
        return ""
