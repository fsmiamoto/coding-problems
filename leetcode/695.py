from collections import deque
from typing import List

LAND = 1
WATER = 0

class Solution:
    # DFS
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      result = 0
      ROWS, COLS = len(grid), len(grid[0])

      def validPosition(row: int, col:int) -> bool:
        return row >= 0 and row < ROWS and col >= 0 and col < COLS

      def islandSize(row: int, col: int, visited) -> int:
        if not validPosition(row,col) or grid[row][col] == WATER or (row,col) in visited:
          return 0

        visited.add((row,col))

        return 1 + islandSize(row+1,col,visited) + islandSize(row-1,col,visited)+islandSize(row,col-1,visited)+islandSize(row,col+1,visited)

      visited = set()
      for row in range(ROWS):
        for col in range(COLS):
          if (row,col) not in visited:
            result = max(result, islandSize(row,col,visited))

      return result


    # BFS
    def _maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        ROWS, COLS = len(grid), len(grid[0])

        def validPosition(row: int, col:int) -> bool:
          return row >= 0 and row < ROWS and col >= 0 and col < COLS

        def islandSize(row: int, col: int, visited) -> int:
          if grid[row][col] == WATER:
            return 0

          queue = deque()
          islandSize = 0
          queue.append((row,col))

          while queue:
            (r, c) = queue.popleft()

            # FIXME: Why adding duplicates?
            if (r,c) in visited:
              continue

            islandSize += 1
            visited.add((r,c))

            for (rowOffset, colOffset) in [(0,1),(0,-1),(1,0),(-1,0)]:
              neighborRow, neighborCol = r+rowOffset, c+colOffset
              if not validPosition(neighborRow, neighborCol) or (neighborRow, neighborCol) in visited or grid[neighborRow][neighborCol] == WATER:
                continue
              queue.append((neighborRow, neighborCol))

          return islandSize

        visited = set()
        for row in range(ROWS):
          for col in range(COLS):
            if (row, col) not in visited:
               result = max(result, islandSize(row,col,visited))

        return result
