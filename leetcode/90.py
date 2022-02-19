from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def do(subset, i):
          if i >= len(nums):
            return [subset]

          head = nums[i]

          with_head = subset.copy()
          with_head.append(head)
          a = do(with_head,i+1)

          # Skip any duplicates on the side that does not include items
          while i+1 < len(nums) and nums[i+1] == nums[i]:
            i += 1
          b = do(subset,i+1)

          return  a + b

        return do([],0)
