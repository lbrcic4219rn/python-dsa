from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                l, r = j + 1, len(nums) - 1
                t = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == t:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < len(nums) and nums[l - 1] == nums[l]:
                            l += 1
                        while r >= 0 and nums[r + 1] == nums[r]:
                            r -= 1
                        continue
                    if nums[l] + nums[r] > t:
                        r -= 1
                    else:
                        l += 1

        return res
