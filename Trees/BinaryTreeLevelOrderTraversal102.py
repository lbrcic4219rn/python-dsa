from collections import deque
from typing import Optional, List

from Trees.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []

        while queue:
            lvl = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl:
                result.append(lvl)
        return result

    def lvlOrderRec(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
