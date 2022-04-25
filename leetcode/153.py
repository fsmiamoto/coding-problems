class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 4 5 6 7 0 1 2
        # T T T T F F F

        left, right = 0, len(nums)-1

        minimum = float('inf')

        while left <= right:
          middle = left + (right-left)//2

          if nums[middle] > nums[right]:
            # Search right
            left = middle +1
          else:
            # Search left
            minimum = min(nums[middle],minimum)
            right = middle - 1

        return minimum
