from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def sameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if None in [a,b]:
            if not a and not b:
                return True

            return False

        return a.val == b.val and self.sameTree(a.left,b.left) and self.sameTree(a.right, b.right)

