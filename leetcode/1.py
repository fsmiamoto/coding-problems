from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for (i,n) in enumerate(nums):
          want = target - n
          if want in indices:
            return [i,indices[want]]

          indices[n] = i

        # NOT REACHED
        return [-1,-1]
