from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right)) + 1

        def check_balanced(root):
            if not root:
                return True
            return check_balanced(root.left) and check_balanced(root.right) and abs(height(root.left)-height(root.right)) <= 1

        return check_balanced(root)

