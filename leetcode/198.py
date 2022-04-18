from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
      self.memo = {}
      def robMemo(index: int):
        if index >= len(nums):
          return 0

        if index in self.memo:
          return self.memo[index]

        self.memo[index] = max(nums[index]+robMemo(index+2),robMemo(index+1))
        return self.memo[index]

      return robMemo(0)
