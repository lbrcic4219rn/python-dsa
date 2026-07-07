from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l - r) > 1:
                res = False
            return 1 + max(l, r)

        dfs(root)
        return res