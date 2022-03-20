from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# Not using constant space tough
# But since this is a iterative solution, we don't have the extra call stack memory so I'd say it's fine :upside_down_face:;x

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()

        if root:
            queue.append(root)
        previousNode = None

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if previousNode:
                    previousNode.next = node
                previousNode = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            previousNode = None

        return root

