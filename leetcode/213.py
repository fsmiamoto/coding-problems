from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return nums[0]

      def _rob(nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
          temp =  max(n+rob1, rob2)
          rob1 = rob2
          rob2 = temp

        return rob2

      return max(_rob(nums[:len(nums)-1]),_rob(nums[1:]))
