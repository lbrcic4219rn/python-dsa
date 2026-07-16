class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        indx = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            nums[indx] = nums[i]
            indx += 1
        return indx
