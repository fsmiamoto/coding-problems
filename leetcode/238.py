from typing import List

# For each position the result would be:
# result[i] = left[i] * right[i]
# Instead of creating two new arrays, lets use the space
# we've allocated for the result array already.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      left = 1
      result = []
      for i in range(len(nums)):
        result.append(left)
        left *= nums[i]

      right = 1
      for i in range(len(nums)-1,-1,-1):
        result[i] *= right
        right *= nums[i]

      return result
