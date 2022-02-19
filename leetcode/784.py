from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      result = 0

      values = {}
      for n in nums:
        values[n] = True

      for n in nums:
        if n-1 in values:
          # Not start of a sequence
          continue

        # Possible sequence
        length = 1
        while True:
          if not (n+length) in values:
            break
          length += 1

        result = max(result,length)

      return result
