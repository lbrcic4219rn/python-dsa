class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i + 1:
                i += 1
                continue

            correct_idx = nums[i] - 1

            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        i = 0
        while i < len(nums) and nums[i] == i + 1:
            i += 1

        return i + 1
