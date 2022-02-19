from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if None in [p, q]:
            if (not p and q) or (p and not q):
                return False

            # Both None
            return True

        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)

        return left and right and p.val == q.val
