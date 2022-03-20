from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], targetSum: int, currentPath: List[int]) -> int:
            if not node:
                return 0

            currentPath.append(node.val)
            pathCount, pathSum = 0,0

            # Find the sums of the subpaths
            for i in range(len(currentPath)-1,-1,-1):
                pathSum += currentPath[i]
                # The subpath has matched our target sum, hooray
                if pathSum == targetSum:
                    pathCount += 1

            pathCount += dfs(node.left, targetSum, currentPath)
            pathCount += dfs(node.right, targetSum, currentPath)

            del currentPath[-1]

            return pathCount

        return dfs(root,targetSum,[])
