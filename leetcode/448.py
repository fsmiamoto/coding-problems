from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                # Do not flip value twice
                nums[index] = -nums[index]

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)

        return result
