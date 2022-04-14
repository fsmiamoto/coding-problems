from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # [left, right)
      left, right = 0, len(nums)

      while left < right:
        middle = (left+right) // 2

        if nums[middle] < target:
          left = middle + 1
        else:
          right = middle

      # invariant: left == right, return either
      if left >= len(nums) or nums[left] != target:
        return -1

      return left
