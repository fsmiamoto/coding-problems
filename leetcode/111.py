from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        result = 0

        if root:
            queue.append(root)

        while len(queue) > 0:
            n = len(queue)
            result += 1
            for _ in range(n):
                elem = queue.popleft()

                if not elem.left and not elem.right:
                    return result

                if elem.left:
                    queue.append(elem.left)
                if elem.right:
                    queue.append(elem.right)

        return result
