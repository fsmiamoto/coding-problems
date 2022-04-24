class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # _ + _ + _ = 0
        nums.sort()
        result = []

        for i, a in enumerate(nums):
          # Skip duplicated values, we don't want the same value as the first position
          if i > 0 and nums[i-1] == a:
            continue

          # threeSum = a + b + c

          # Two sum on sorted input
          left, right = i+1, len(nums)-1
          while left < right:
            b, c = nums[left], nums[right]
            threeSum = a + b + c
            if threeSum < 0:
              left += 1
            elif threeSum > 0:
              right -= 1
            else:
              result.append([a,b,c])
              # Move left pointer
              left += 1
              # Skip duplicates again, we dont want the same value in b position
              while left < len(nums) and nums[left-1] == nums[left] and left < right:
                left += 1

        return result
