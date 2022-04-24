class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left <= right:
          middle = (left+right)//2

          if nums[middle] == target:
            return middle

          if nums[left] <= nums[middle]:
            # In left sorted portion
            if target > nums[middle] or target < nums[left]:
              # Search right
              left = middle + 1
            else:
              right = middle - 1
          else:
            # In right sorted portion
            if target < nums[middle] or target > nums[right]:
              right = middle - 1
            else:
              left = middle + 1

        return -1
