from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        num = 0

        def dfs(node):
            nonlocal count, num
            if not node:
                return

            dfs(node.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                num = node.val
                return
            dfs(node.right)

        dfs(root)
        return num
