from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       result, maxsum = nums[0], nums[0]
       for n in nums[1:]:
           result = max(result+n, n)
           if result > maxsum:
                maxsum = result
       return maxsum
