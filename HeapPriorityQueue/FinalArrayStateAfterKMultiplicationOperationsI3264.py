import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minHeap)

        for i in range(k):
            val, index = heapq.heappop(minHeap)
            nums[index] = val * multiplier
            heapq.heappush(minHeap, (nums[index], index))

        return nums
