from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        queue.append(root)
        avgs = []

        while len(queue) > 0:
            n = len(queue)
            summation, count = 0.0, 0
            for _ in range(n):
                first = queue.popleft()
                summation += first.val
                count += 1

                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)

            avgs.append(summation/count)

        return avgs
