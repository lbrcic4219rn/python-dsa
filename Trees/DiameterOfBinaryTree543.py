from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            res = max(res, l + r)

            return 1 + max(l, r)

        dfs(root)
        return res
