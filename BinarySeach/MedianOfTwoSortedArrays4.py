from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        if len(a) >= len(b):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            aIndex = l + (r - l) // 2
            bIndex = half - aIndex
            aLeft = a[aIndex] if aIndex >= 0 else float("-infinity")
            aRight = a[aIndex + 1] if aIndex + 1 < len(b) else float("infinity")
            bLeft = b[aIndex] if bIndex >= 0 else float("-infinity")
            bRight = b[aIndex + 1] if bIndex + 1 < len(b) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = aIndex - 1
            else:
                l = aIndex + 1