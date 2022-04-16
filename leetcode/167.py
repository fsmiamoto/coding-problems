from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      left, right = 0, len(numbers)-1

      while left < right:
        _sum = numbers[left] + numbers[right]
        if _sum > target:
          # Decrease it, move right pointer
          right -= 1
        elif _sum < target:
          left += 1
        else:
          # Found solution, left < right
          return [left+1, right+1]

      # NOT REACHED
      return [-1,-1]
