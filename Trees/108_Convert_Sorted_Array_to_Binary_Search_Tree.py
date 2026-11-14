from typing import List, Optional

from Trees.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(l, r):
            nonlocal nums

            if l > r:
                return None

            m = l + (r - l) // 2

            root = TreeNode(nums[m])
            root.left = construct(l, m - 1)
            root.right = construct(m + 1, r)

            return root

        return construct(0, len(nums) - 1)
