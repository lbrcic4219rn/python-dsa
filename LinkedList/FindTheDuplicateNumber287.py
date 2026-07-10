class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        beg = 0
        while beg != slow:
            beg = nums[beg]
            slow = nums[slow]
        return nums[slow]
