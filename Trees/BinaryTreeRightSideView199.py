from collections import deque
from typing import Optional, List

from Trees.TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            rightMost = None
            for _ in range(len(q)):
                node = q.popleft()
                rightMost = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if rightMost:
                res.append(rightMost.val)

        return res