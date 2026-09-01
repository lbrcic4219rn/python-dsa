from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        min_len = len(nums)
        seen = {0: -1}

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target) % p

            if needed in seen:
                min_len = min(min_len, i - seen[needed])

            seen[prefix] = i

        return min_len if min_len < len(nums) else -1
