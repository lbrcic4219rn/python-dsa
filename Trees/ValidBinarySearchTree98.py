from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not root:
                return True

            if not lower < root.val < upper:
                return False

            left = dfs(root.left, lower, root.val)
            right = dfs(root.right, root.val, upper)

            return left and right

        return dfs(root, float("-inf"), float("inf"))
