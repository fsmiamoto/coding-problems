from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      def addOne(digits: List[int], position: int):
        if position == -1:
          digits.insert(0,1)
          return

        digits[position] += 1
        if digits[position] >= 10:
          digits[position] = digits[position] % 10
          addOne(digits, position-1)
        return
      addOne(digits,len(digits)-1)
      return digits
