class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        for num in nums:
            i = 1
            while (num + i) in hashSet:
                i += 1
            res = max(i, res)

        return res