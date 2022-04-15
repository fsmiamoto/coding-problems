from collections import deque
from math import floor, ceil
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      operators = {
        "+": lambda x,y : x+y,
        "-": lambda x,y : x-y,
        "/": lambda x,y : x/y,
        "*": lambda x,y : x*y,
      }

      stack = deque()

      for token in tokens:
        if token not in operators:
          stack.append(int(token))
          continue

        operator = operators[token]

        b = stack.pop()
        a = stack.pop()
        result = operator(a,b)
        truncated = floor(result) if result > 0 else ceil(result)

        stack.append(truncated)

      return stack.pop()
