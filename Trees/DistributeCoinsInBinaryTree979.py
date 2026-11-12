from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            cnt += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return cnt