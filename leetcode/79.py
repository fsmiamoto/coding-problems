from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      rows = len(board)
      cols = len(board[0])
      path = set()

      def valid(row: int, col: int) -> bool:
        return row >= 0 and row < rows and col >= 0 and col < cols

      def dfs(row: int, col: int, wordIndex: int) -> bool:
        if wordIndex == len(word):
          return True

        if not valid(row,col) or (row,col) in path or word[wordIndex] != board[row][col]:
          return False

        path.add((row,col))

        result = dfs(row+1,col,wordIndex+1) or dfs(row-1,col,wordIndex+1) or dfs(row,col+1, wordIndex+1) or dfs(row,col-1, wordIndex+1)

        path.remove((row,col))
        return result

      for i in range(rows):
        for j in range(cols):
          if dfs(i,j,0):
            return True

      return False
