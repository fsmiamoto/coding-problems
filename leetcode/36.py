from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        def checkRows(board: List[List[str]]) -> bool:
          for row in range(n):
            seen = set()
            for col in range(n):
              if board[row][col] in seen:
                return False
              if board[row][col] != '.':
                seen.add(board[row][col])
          return True

        def checkCols(board: List[List[str]]) -> bool:
          for col in range(n):
            seen = set()
            for row in range(n):
              if board[row][col] in seen:
                return False
              if board[row][col] != '.':
                seen.add(board[row][col])
          return True

        def checkBoxes(board: List[List[str]]) -> bool:
          for rowMul in range(1,4):
                for colMul in range(1,4):
                  seen = set()
                  for row in range(3*(rowMul-1),3*rowMul):
                    for col in range(3*(colMul-1),3*colMul):
                      if board[row][col] in seen:
                        return False
                      if board[row][col] != '.':
                        seen.add(board[row][col])
          return True

        return checkRows(board) and checkCols(board) and checkBoxes(board)
