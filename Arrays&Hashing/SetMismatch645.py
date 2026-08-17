from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        present = set()

        res = []
        for num in nums:
            if num in present:
                res.append(num)
            present.add(num)

        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)

        return res
