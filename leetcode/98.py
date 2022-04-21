from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # Use the fact that a in-order traversal must be in sorted order
        def inorder(root):
            if not root:
                return True

            left = inorder(root.left)
            if not left:
                return False

            if self.prev and self.prev.val >= root.val:
                return False

            self.prev = root

            right = inorder(root.right)
            if not right:
                return False

            return True

        return inorder(root)

    # Using min-max
    def _isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def checkTree(root: Optional[TreeNode], min, max):
            if not root:
                return True

            if root.val <= min or root.val >= max:
                return False

            return checkTree(root.left, min, root.val) and checkTree(root.right, root.val, max)

        return checkTree(root, float('-inf'), float('inf'))
