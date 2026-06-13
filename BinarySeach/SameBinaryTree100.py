from typing import Optional
from Trees.TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (p and not q) or (not p and q):
            return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        isSame = p.val == q.val

        return isLeftSame and isRightSame and isSame
