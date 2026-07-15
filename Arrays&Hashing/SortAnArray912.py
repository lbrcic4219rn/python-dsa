from typing import List


class Solution:
    def merge(self, nums, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = nums[l + i]
        for i in range(n2):
            R[i] = nums[m + 1 + i]

        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        m = l + (r - l) // 2
        self.mergeSort(nums, l, m)
        self.mergeSort(nums, m + 1, r)
        self.merge(nums, l, m, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)

        return nums
