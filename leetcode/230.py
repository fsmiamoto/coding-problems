from heapq import heappush, heappop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-order traversal - return when k elements are in the result
        self.traversal = []

        def traverse(root: Optional[TreeNode]):
            # Return when length of self.traversal is k
            if not root:
                return

            if len(self.traversal) == k:
                return
            traverse(root.left)
            if len(self.traversal) == k:
                return
            self.traversal.append(root.val)
            if len(self.traversal) == k:
                return
            traverse(root.right)

        traverse(root)
        return self.traversal[-1]
