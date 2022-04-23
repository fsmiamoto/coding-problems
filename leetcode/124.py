from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      maxSum = float('-inf')

      def traverse(node: Optional[TreeNode]):
        nonlocal maxSum

        if not node:
          return 0

        # If the sums are negative, just ignore them
        leftSum = max(0,traverse(node.left))
        rightSum = max(0,traverse(node.right))

        localMax = node.val + leftSum + rightSum

        maxSum = max(maxSum, localMax)

        return node.val + max(leftSum, rightSum)

      traverse(root)

      return int(maxSum)
