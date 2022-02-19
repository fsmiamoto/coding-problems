from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
          # Since values are in the range [1,n], subtracting one will
          # yield values in the range [0,n-1] which are valid indices
          index = abs(nums[i])-1
          if nums[index] > 0:
            nums[index] = -nums[index]
          else:
            result.append(index+1)

        return result
