"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        visited = set()
        def dfs(node: 'Node'):
            if not node or node.val in visited:
                return

            newNode = Node(node.val)
            oldToNew[node.val] = newNode

            visited.add(node.val)

            for neighbor in node.neighbors:
                dfs(neighbor)

            for neighbor in node.neighbors:
                newNode.neighbors.append(oldToNew[neighbor.val])

        dfs(node)
        return oldToNew[node.val] if node else None
