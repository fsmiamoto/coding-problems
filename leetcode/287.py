from typing import List

class Solution:
    def _findDuplicate(self, nums: List[int]) -> int:
      # This works but it is not allowed since we can't modify the array
      n = len(nums)
      for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
          nums[index] = -nums[index]
        else:
          return index+1

      # NOT REACHED
      return -1

    def findDuplicate(self, nums: List[int]) -> int:
      # Floyd's tortoise and hare algorithm
      slow, fast = 0,0
      while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
          break

      fast = 0
      while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

      return fast
