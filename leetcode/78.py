from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def do(subset, i):
          if i >= len(nums):
            return [subset]

          head = nums[i]
          with_head = subset.copy()
          with_head.append(head)

          return do(subset,i+1) + do(with_head,i+1)

        return do([],0)
