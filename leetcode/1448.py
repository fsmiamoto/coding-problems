from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

MIN_VALUE=-(1E5)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0

        def traverse(root: Optional[TreeNode], largestValueInPath: int):
            # Check if the larget value in the path is not greater than the node value
            # If so, increment the result
            if not root:
                return

            if largestValueInPath <= root.val:
                self.result += 1

            largest =  max(root.val, largestValueInPath)
            traverse(root.left, largest)
            traverse(root.right, largest)

        traverse(root, MIN_VALUE)

        return self.result
