from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check_balanced(root):
            if not root:
                return (True, 0)

            left = check_balanced(root.left)
            right = check_balanced(root.right)

            balanced = abs(left[1]-right[1]) <= 1

            return (left[0] and right[0] and balanced, max(left[1],right[1])+1)

        return check_balanced(root)[0]
