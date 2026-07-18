from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root, val):
            if not root:
                return TreeNode(val)
            if root.val > val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root

        return insert(root, val)
