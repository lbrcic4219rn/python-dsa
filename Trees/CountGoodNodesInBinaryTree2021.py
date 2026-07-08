from Trees.TreeNode import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return
            if node.val >= maxVal: count += 1
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))

        dfs(root, -101)
        return count
