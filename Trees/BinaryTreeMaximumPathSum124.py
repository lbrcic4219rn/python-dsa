from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            maxSum = max(maxSum, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)
        return maxSum
