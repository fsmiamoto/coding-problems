from typing import List

# For each position the result would be:
# result[i] = prefix[i] * postfix[i]
# Instead of creating two new arrays, lets use the space
# we've allocated for the result array already.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n = len(nums)
      result = [1] * n

      prefix = 1
      for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

      postfix = 1
      for i in range(n-1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

      return result
