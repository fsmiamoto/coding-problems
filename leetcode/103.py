from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        # Zig: left -> right
        # Zag: right -> left
        zig = True

        while queue:
            n = len(queue)
            levelNodes = deque()

            for _ in range(n):
                node = queue.popleft()
                if zig:
                    levelNodes.append(node.val)
                else:
                    levelNodes.appendleft(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            zig = not zig
            result.append(list(levelNodes))

        return result
