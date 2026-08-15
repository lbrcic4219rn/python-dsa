from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        present = set()
        for num in nums:
            present.add(num)
        res = []
        for i in range(1, n + 1):
            if i not in present:
                res.append(i)

        return res
