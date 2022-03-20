from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(currentNode: Optional[TreeNode], targetSum: int, currentPath: List[int]):
            if not currentNode:
                return

            currentPath.append(currentNode.val)

            if currentNode.val == targetSum and not currentNode.left and not currentNode.right:
                result.append(currentPath.copy())
            else:
                newTarget = targetSum - currentNode.val
                dfs(currentNode.left, newTarget, currentPath)
                dfs(currentNode.right, newTarget, currentPath)

            # Remove the current val from path for backtracking.
            del currentPath[-1]

        dfs(root,targetSum, [])

        return result
