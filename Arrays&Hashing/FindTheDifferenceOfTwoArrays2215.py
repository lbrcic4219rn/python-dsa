from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        setA = set(nums1)
        setB = set(nums2)

        res.append(setA.difference(setB))
        res.append(setB.difference(setA))

        return res
