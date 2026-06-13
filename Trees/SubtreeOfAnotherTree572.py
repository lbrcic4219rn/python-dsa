from typing import Optional

from Trees.TreeNode import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while len(queue) != 0:
            treeNode = queue.pop()
            if treeNode.val == subRoot.val:
                if self.isTheSameTree(treeNode, subRoot):
                    return True

            if treeNode.left:
                queue.append(treeNode.left)
            if treeNode.right:
                queue.append(treeNode.right)
        return False

    def isTheSameTree(self, p, q):
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        left = self.isTheSameTree(p.left, q.left)
        right = self.isTheSameTree(p.right, q.right)
        same = p.val == q.val
        return left and right and same

    def isSubtreeRecursive(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isTheSameTree(root, subRoot):
            return True

        return (self.isSubtreeRecursive(root.left, subRoot)
                or self.isSubtreeRecursive(root.right, subRoot))
