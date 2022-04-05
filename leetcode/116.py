from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            levelCount = len(queue)
            prevNode = None
            for _ in range(levelCount):
                node = queue.popleft()
                if prevNode:
                    prevNode.next = node
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                prevNode = node

        return root
