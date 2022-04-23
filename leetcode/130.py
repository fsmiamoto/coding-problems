from typing import List

class Solution:
    # Reverse thinking
    def solve(self, grid: List[List[str]]) -> None:
      ROWS, COLS = len(grid), len(grid[0])

      def validPosition(row: int,col: int)->bool:
        return row >= 0 and row < ROWS and col >= 0 and col < COLS

      def isBorder(row: int, col: int) -> bool:
        return row == 0 or row == ROWS-1 or col == 0 or col == COLS-1

      def markUnsurroundedRegion(row: int, col: int, visited):
        if not validPosition(row,col) or grid[row][col] != 'O':
          return

        # Temporary
        grid[row][col] = 'T'
        visited.add((row,col))

        markUnsurroundedRegion(row+1,col, visited)
        markUnsurroundedRegion(row-1,col, visited)
        markUnsurroundedRegion(row,col+1, visited)
        markUnsurroundedRegion(row,col-1, visited)

      # Only keep the 'O' at the border
      visited = set()
      for row in range(ROWS):
        for col in range(COLS):
          if grid[row][col] == 'O' and isBorder(row,col):
            markUnsurroundedRegion(row,col,visited)

      for row in range(ROWS):
        for col in range(COLS):
          if grid[row][col] == 'O':
            grid[row][col] = 'X'
          elif grid[row][col] == 'T':
            grid[row][col] = 'O'
