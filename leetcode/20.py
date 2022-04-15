class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
          # Odd number of characters
          return False

        pairs = {
          '(': ')',
          '{': '}',
          '[': ']',
        }

        stack = []
        for char in s:
          if char in pairs:
            stack.append(pairs[char])
            continue

          if not stack:
            # Closing char but stack is empty, invalid
            return False

          expect = stack.pop()
          if char != expect:
            return False

        # Stack should be empty
        return not stack
